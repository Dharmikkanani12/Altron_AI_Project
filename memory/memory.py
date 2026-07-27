"""
Memory — short-term (current conversation) and long-term (persistent) storage.
"""

import json
import os
import sqlite3
from datetime import datetime

from core import config


class ShortTermMemory:
    """Holds the current conversation only. Cleared on restart."""

    def __init__(self, max_messages: int = config.MAX_SHORT_TERM_MESSAGES):
        self.max_messages = max_messages
        self.messages: list[dict] = []

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_context(self) -> list[dict]:
        return self.messages

    def clear(self):
        self.messages = []


class LongTermMemory:
    """
    Persistent memory backed by SQLite.

    Example:
        ltm = LongTermMemory()
        ltm.remember("project", "Python OS Simulator")
        ltm.recall("project")  -> "Python OS Simulator"
    """

    def __init__(self, db_path: str = config.DATABASE_PATH):
        os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self._init_table()

    def _init_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS facts (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def remember(self, key: str, value):
        self.conn.execute(
            """
            INSERT INTO facts (key, value, updated_at) VALUES (?, ?, ?)
            ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at
            """,
            (key, json.dumps(value), datetime.utcnow().isoformat()),
        )
        self.conn.commit()

    def recall(self, key: str):
        row = self.conn.execute(
            "SELECT value FROM facts WHERE key = ?", (key,)
        ).fetchone()
        return json.loads(row[0]) if row else None

    def forget(self, key: str):
        self.conn.execute("DELETE FROM facts WHERE key = ?", (key,))
        self.conn.commit()
