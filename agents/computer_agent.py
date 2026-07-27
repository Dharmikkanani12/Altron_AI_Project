"""
Computer Agent — controls the PC: mouse, keyboard, files, applications, browser.

Caution: this agent has real system access once implemented. Guard any
destructive actions (deleting files, running arbitrary commands) behind
explicit user confirmation.
"""

from agents.agent import Agent
from tools import system_control


class ComputerAgent(Agent):
    name = "computer_agent"

    def run(self, task: str) -> str:
        # TODO: parse `task` into an action (open_app, click, type, etc.)
        # and dispatch to tools/system_control.py.
        return system_control.open_application(task)
