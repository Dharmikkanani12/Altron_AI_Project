"""
Central configuration for ALTRON.

Loads settings from environment variables (via a .env file if present).
Create a .env file in the project root:

    MODEL_PROVIDER=openai
    OPENAI_API_KEY=sk-...
    MODEL_NAME=gpt-4o-mini
"""

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed yet — fine, just relies on real env vars
    pass


MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "openai")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
API_KEY = os.getenv("OPENAI_API_KEY", "")

# Memory settings
MAX_SHORT_TERM_MESSAGES = 20

# Database
DATABASE_PATH = os.getenv("DATABASE_PATH", "database/memory.db")
