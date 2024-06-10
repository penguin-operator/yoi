from __future__ import annotations
import tkinter as tk
import yoi.widgets.tab as tab
from yoi.util.geometry_data import geometry_data

class TabSystem(tk.Frame):
    def __init__(self, master: tk.Misc, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        self.__titlebar__ = tk.Frame(self)
        self.__tabs__ = []
        self.__titlebar__.pack(side="top", fill='x')

    @property
    def tabs(self):
        return self.__tabs__

    def add(self, tab: "tab.Tab"):
        self.__tabs__.append(tab)

    def open(self, tab: "tab.Tab | int"):
        for t in self.__tabs__:
            t.forget()
        if isinstance(tab, int):
            if len(self.__tabs__) == 0:
                return
            tab: "tab.Tab" = self.__tabs__[tab]
        elif tab not in self.__tabs__:
            self.__tabs__.append(tab)
        manager, data = geometry_data(tab)
        if manager:
            getattr(tab, manager).__call__(**data)
        else:
            tab.pack(fill="both", expand=True)

    def close(self, tab: "tab.Tab | int"):
        if isinstance(tab, int):
            index = tab
            tab: "tab.Tab" = self.__tabs__[tab]
        else:
            index = self.__tabs__.index(tab)
        self.__tabs__.remove(tab)
        if index == len(self.__tabs__):
            index -= 1
        tab.__title__.destroy()
        tab.destroy()
        self.open(index)
