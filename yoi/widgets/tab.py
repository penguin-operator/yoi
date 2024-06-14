from __future__ import annotations
import tkinter as tk
import yoi.widgets.tabsystem as tabsystem
from yoi.widgets.tabtitle import TabTitle

class Tab(tk.Frame):
    def __init__(self, master: "tabsystem.TabSystem", cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        self.master: "tabsystem.TabSystem" = master
        self.__title__ = TabTitle(master.__titlebar__, self)
        self.__title__.pack(side="left")
        self.master.open(self)

    def title(self, text: str = "") -> str:
        if text:
            self.__title__.children["!button"]["text"] = text
        return self.__title__.children["!button"]["text"]

    def open(self):
        self.master.open(self)

    def close(self):
        self.master.close(self)
