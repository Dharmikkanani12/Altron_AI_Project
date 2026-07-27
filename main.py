"""
ALTRON AI — entry point.

Phase 1 loop:
    User -> GUI -> AI Brain -> Memory -> Response

Run:
    python main.py
"""

import argparse

from core.brain import Brain
from memory.memory import ShortTermMemory
from gui.app import AltronGUI


def run_cli():
    """Simple command-line chat loop for quick chatbot use."""
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


def run_gui():
    """Launch the graphical chatbot window."""
    import tkinter as tk

    root = tk.Tk()
    AltronGUI(root)
    root.mainloop()


def main():
    parser = argparse.ArgumentParser(description="Run ALTRON chatbot.")
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Start the graphical chat bot interface",
    )
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        run_cli()


if __name__ == "__main__":
    main()
