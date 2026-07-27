"""
GUI — the chat face of ALTRON.

Stub built with tkinter (ships with Python, no extra install needed).
Swap for PyQt/customtkinter later if you want a nicer look.

Run directly:
    python gui/app.py
"""

import tkinter as tk

from core.brain import Brain
from memory.memory import ShortTermMemory


class AltronGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ALTRON AI")

        self.brain = Brain()
        self.memory = ShortTermMemory()

        self.chat_log = tk.Text(root, width=60, height=25, state="disabled")
        self.chat_log.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(side="left", padx=(10, 0), pady=(0, 10))
        self.entry.bind("<Return>", self.on_send)

        self.send_button = tk.Button(root, text="Send", command=self.on_send)
        self.send_button.pack(side="left", padx=10, pady=(0, 10))

    def on_send(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.entry.delete(0, tk.END)

        self.memory.add("user", user_input)
        response = self.brain.think(user_input, context=self.memory.get_context())
        self.memory.add("assistant", response)

        self._append(f"You: {user_input}")
        self._append(f"ALTRON: {response}\n")

    def _append(self, text: str):
        self.chat_log.configure(state="normal")
        self.chat_log.insert(tk.END, text + "\n")
        self.chat_log.configure(state="disabled")
        self.chat_log.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    AltronGUI(root)
    root.mainloop()
