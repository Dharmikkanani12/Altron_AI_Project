"""
Research Agent — finds information, summarizes, compares ideas, builds reports.
"""

from agents.agent import Agent


class ResearchAgent(Agent):
    name = "research_agent"

    def run(self, task: str) -> str:
        # TODO: hook up a web search tool (e.g. requests + a search API)
        # and feed results into Brain.think() for summarization.
        return f"(placeholder) ResearchAgent would now research: '{task}'"
