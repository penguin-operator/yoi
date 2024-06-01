from __future__ import annotations
import tkinter as tk
import yoi.widgets.tabsystem as tabsystem

class Tab(tk.Frame):
    def __init__(self, master: "tabsystem.TabSystem", cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        self.__title__ = tk.Frame(master.__titlebar__)
        title = tk.Button(self.__title__, text=self.__class__.__name__, command=self.open)
        title.pack(side="left")
        close = tk.Button(self.__title__, text="x", command=self.close)
        close.pack(side="right")
        self.__title__.pack(side="left")
        self.master.open(self)

    def open(self):
        self.master.open(self)

    def close(self):
        self.master.close(self)
