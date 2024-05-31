from __future__ import annotations
import tkinter as tk
import yoi.widgets.tab as tab

class TabSystem(tk.Frame):
    def __init__(self, master: tk.Misc, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        self.title = tk.Frame(self)
        self.space = tk.Frame(self)
        self.tabs = []
        self.title.pack(side="top", fill='x')
        self.space.pack(side="bottom", fill="both", expand=True)

    def add(self, tab: "tab.Tab"):
        self.tabs.append(tab)
