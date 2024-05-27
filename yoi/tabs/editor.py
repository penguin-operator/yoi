import tkinter as tk
from .tab import Tab
from utils import keypad

class Editor(Tab):
    def __init__(self):
        Tab.__init__(self)
        self.title("Untitled")
        self.lines = tk.Text(self, width=4, state="disabled")
        self.lines.pack(side="left", fill="y", expand=False)
        self.editor = keypad(tk.Text(self))
        self.editor.bind("<Key>", lambda _: self.after(1, self.__lines__))
        self.editor.pack(side="right", fill="both", expand=True)

    def __lines__(self):
        lines = self.editor.get("1.0", "end").count('\n')
        self.lines["state"] = "normal"
        self.lines.delete("1.0", "end")
        self.lines.insert("1.0", '\n'.join(map(str, range(1, lines + 1))))
        self.lines["state"] = "disabled"
