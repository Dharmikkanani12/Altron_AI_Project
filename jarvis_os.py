"""Jarvis OS entrypoint for the Altron AI assistant.

This script provides a Jarvis-style CLI wrapper that uses the same core
brain and short-term memory as `main.py`.
"""

from core.brain import Brain
from memory.memory import ShortTermMemory


def run_jarvis():
    print("JARVIS OS — type 'exit' to quit.\n")

    brain = Brain()
    memory = ShortTermMemory()

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("JARVIS: Goodbye.")
            break

        memory.add("user", user_input)
        response = brain.think(user_input, context=memory.get_context())
        memory.add("assistant", response)

        print(f"JARVIS: {response}\n")


if __name__ == "__main__":
    run_jarvis()
