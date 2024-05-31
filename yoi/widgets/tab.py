from __future__ import annotations
import tkinter as tk
import yoi.widgets.tabsystem as tabsystem

class Tab(tk.Widget):
    def __init__(self, master: "tabsystem.TabSystem", cnf={}, **kw):
        tk.Widget.__init__(self, master.space, "tab", cnf, **kw)
        self.master = master.master
