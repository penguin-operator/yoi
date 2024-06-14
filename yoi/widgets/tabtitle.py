from __future__ import annotations
import tkinter as tk
import yoi.widgets.tab as tab

class TabTitle(tk.Frame):
    def __init__(self, master: tk.Misc, tab: "tab.Tab", text: str = "Tab", cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        self.label = tk.Button(self, text=text, command=lambda: tab.open())
        self.label.pack(side="left")
        self.close = tk.Button(self, text="x", command=lambda: tab.close())
        self.close.pack(side="right")
