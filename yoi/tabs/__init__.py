import tkinter as tk
from .tab import Tab
from .settings import Settings
from .welcome import Welcome

class Tabs(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        Tab.master = self
        self.titlebar = tk.Frame(self)
        self.titlebar.pack(side="top", fill="x")
        self.tabs = []

    def add(self, tab: Tab):
        titlebar = tk.Frame(self.titlebar)
        title = tk.Button(titlebar, text="")
        title["command"] = lambda i=len(self.tabs): self.open(i)

        self.tabs.append((tab, titlebar, {}))
        self.open(len(self.tabs) - 1)

        title.pack(side="left", fill="x")
        titlebar.pack(side="left", fill="x")
    
    def open(self, i: int):
        for j, (tab, *_) in enumerate(self.tabs):
            if j == i:
                tab.pack(fill="both", expand=1, ipadx=2, ipady=2)
            else:
                tab.forget()

    def title(self, tab: Tab, title: str) -> str | None:
        for i, (t, titlebar, _) in enumerate(self.tabs):
            if t == tab:
                if title == "":
                    return titlebar.children["!button"]["text"]
                titlebar.children["!button"]["text"] = title
