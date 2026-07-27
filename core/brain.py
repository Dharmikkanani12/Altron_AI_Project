"""
The AI Brain — ALTRON's thinking center.

Flow:
    User Question -> understand request -> plan steps -> give solution
"""

from core import config
from core.planner import plan_steps

try:
    import openai
except ImportError:  # pragma: no cover
    openai = None


class Brain:
    def __init__(self):
        self.provider = config.MODEL_PROVIDER.strip().lower()
        self.model_name = config.MODEL_NAME
        self.api_key = config.API_KEY

    def think(self, user_input: str, context: list | None = None) -> str:
        """
        Main reasoning entry point.

        1. (Optional) break the request into steps via the planner
        2. Call the connected model
        3. Return the response
        """
        steps = plan_steps(user_input)
        response = self.call_model(user_input, context=context, steps=steps)
        return response

    def call_model(self, user_input: str, context=None, steps=None) -> str:
        """
        Call the configured model provider.
        """
        if self.provider == "openai":
            return self._call_openai(user_input, context=context, steps=steps)

        return (
            f"(placeholder response) I heard: '{user_input}'. "
            "Wire up core/brain.py:call_model() to a real model to make me think."
        )

    def _call_openai(self, user_input: str, context=None, steps=None) -> str:
        if openai is None:
            return (
                "(placeholder response) OpenAI package is not installed. "
                "Install openai and restart."
            )

        if not self.api_key:
            return (
                "(placeholder response) OPENAI_API_KEY is not configured. "
                "Set it in your environment or .env file."
            )

        openai.api_key = self.api_key

        messages = []
        if context:
            messages.extend(context)

        messages.append({"role": "user", "content": user_input})

        if steps:
            messages.insert(0, {
                "role": "system",
                "content": (
                    "You are ALTRON, a helpful AI assistant. "
                    "Use the following plan steps to structure your answer: "
                    f"{steps}"
                ),
            })

        try:
            completion = openai.ChatCompletion.create(
                model=self.model_name,
                messages=messages,
                max_tokens=512,
                n=1,
                temperature=0.7,
            )
            return completion.choices[0].message.content.strip()
        except Exception as exc:
            return f"(error) OpenAI request failed: {exc}"
