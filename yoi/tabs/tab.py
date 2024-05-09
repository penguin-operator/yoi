import tkinter as tk

class Tab(tk.Frame):
    def __init__(self):
        super().__init__(self.master)
        self.master.add(self)

    def title(self, title: str = "") -> str | None:
        return self.master.title(self, title)
