"""
Terminal tool — run shell commands on behalf of agents.

Caution: this executes arbitrary commands. Add allow-listing or user
confirmation before wiring this into an agent that acts autonomously.
"""

import subprocess


def run_command(command: str, timeout: int = 30) -> str:
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        output = result.stdout
        if result.returncode != 0:
            output += f"\n[stderr]\n{result.stderr}"
        return output
    except subprocess.TimeoutExpired:
        return f"Command timed out after {timeout}s: {command}"
