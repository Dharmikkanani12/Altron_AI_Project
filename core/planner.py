"""
Planner — breaks a user request into actionable steps.

Right now this is a simple placeholder. As agents come online (Phase 5),
this is where you'd route a request to the right agent based on intent,
e.g. "make a calculator" -> Coding Agent.
"""


def plan_steps(user_input: str) -> list[str]:
    """
    Return a naive single-step plan.

    TODO: expand this into real intent detection / routing once
    agents/ is wired up, e.g.:
        if "code" in user_input.lower():
            return ["route_to_coding_agent"]
    """
    return [f"respond_to: {user_input}"]
