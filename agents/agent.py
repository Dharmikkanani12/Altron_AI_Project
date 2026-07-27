"""
Base Agent class — all specialized agents inherit from this.
"""

from abc import ABC, abstractmethod


class Agent(ABC):
    name: str = "base_agent"

    @abstractmethod
    def run(self, task: str) -> str:
        """Execute the given task and return a result string."""
        raise NotImplementedError
