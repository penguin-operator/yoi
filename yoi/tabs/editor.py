import tkinter as tk
from .tab import Tab
from utils import keypad

class Editor(Tab):
    def __init__(self):
        Tab.__init__(self)
        self.title("Unsaved *")
        self.lines = tk.Text(self, width=4, state="disabled")
        self.lines.pack(side="left", fill="y", expand=False)
        self.editor = keypad(tk.Text(self))
        self.editor.pack(side="right", fill="both", expand=True)
