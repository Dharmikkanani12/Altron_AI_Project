"""
ALTRON AI — entry point.

Phase 1 loop:
    User -> GUI -> AI Brain -> Memory -> Response

Run:
    python main.py
"""

from core.brain import Brain
from memory.memory import ShortTermMemory


def run_cli():
    """Simple command-line chat loop (swap for gui/app.py when ready)."""
    print("ALTRON AI — type 'exit' to quit.\n")

    brain = Brain()
    memory = ShortTermMemory()

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("ALTRON: Goodbye.")
            break

        memory.add("user", user_input)
        response = brain.think(user_input, context=memory.get_context())
        memory.add("assistant", response)

        print(f"ALTRON: {response}\n")


if __name__ == "__main__":
    run_cli()
