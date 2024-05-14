import tkinter as tk
from tabs.tab import Tab

class TabSystem(tk.Frame):
    __instance__ = None

    def __new__(cls, master):
        if not cls.__instance__:
            cls.__instance__ = tk.Frame.__new__(cls)
        Tab.master = cls.__instance__
        return cls.__instance__

    def __init__(self, master: tk.Tk):
        tk.Frame.__init__(self, master)
        self.titlebar: tk.Frame = tk.Frame(self)
        self.space: tk.Frame = tk.Frame(self)
        self.tabs: list[Tab] = []
        self.titlebar.pack(side="top", fill="x")
        self.space.pack(fill="both", expand=True)

    def add(self, tab: Tab):
        self.tabs.append(tab)
        self.select(tab)
    
    def select(self, tab: Tab):
        for t in self.tabs:
            t.__actions__.forget()
            t.forget()
        tab.__actions__.pack(side="right")
        tab.pack(fill="both", expand=1)

    def close(self, tab: Tab):
        tab.__actions__.destroy()
        tab.destroy()
        self.tabs.remove(tab)
