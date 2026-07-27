"""
Coding Agent — writes, debugs, and explains code; scaffolds projects.

Example (intended):
    agent = CodingAgent()
    agent.run("Make a calculator")
    -> creates files, writes Python, runs tests
"""

from agents.agent import Agent


class CodingAgent(Agent):
    name = "coding_agent"

    def run(self, task: str) -> str:
        # TODO: call Brain with a coding-specific prompt, then use
        # tools/files.py to write the generated code to disk and
        # tools/terminal.py to run tests.
        return f"(placeholder) CodingAgent would now write code for: '{task}'"
