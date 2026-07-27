"""
Workflow automation — chain steps together for repeated tasks.

Example (intended):
    morning_workflow = Workflow([
        "check_emails",
        "create_summary",
        "make_daily_plan",
    ])
    morning_workflow.run()
"""


class Workflow:
    def __init__(self, steps: list[str]):
        self.steps = steps

    def run(self):
        results = []
        for step in self.steps:
            # TODO: map each step name to a real function call
            # (an agent, a tool, or a Brain prompt).
            results.append(f"(placeholder) ran step: {step}")
        return results
