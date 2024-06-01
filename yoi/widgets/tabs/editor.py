import tkinter as tk
from yoi.widgets.tab import Tab
from yoi.widgets.tabsystem import TabSystem

class Editor(Tab):
    def __init__(self, master: TabSystem, cnf={}, **kw):
        Tab.__init__(self, master, cnf, **kw)
        self.editor = tk.Text(self)
        self.number = tk.Text(self, width=4, state="disabled")
        self.number.pack(side="left", fill="y")
        self.editor.pack(fill="both", expand=True)
        self.editor.bind("<KeyPress>", self.update)
        self.editor.bind("<KeyRelease>", self.update)

    def update(self, _):
        self.number["state"] = "normal"
        self.number.delete("1.0", "end")
        lines = self.editor.get("1.0", "end").count("\n")
        first = self.editor.get("1.0")
        if lines > 1 or first != "\n":
            self.number.insert("1.0", '\n'.join(map(str, range(1, lines + 1))))
        self.number["state"] = "disabled"
