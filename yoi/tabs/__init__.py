import tkinter as tk
from tkinter import ttk
from typing import Callable

from .tab import Tab
from .settings import Settings
from .welcome import Welcome

class Tabs(ttk.Notebook):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        Tab.master = self

    def add(self, child: tk.Widget, actions: list[str, Callable] = [], *, text: str = "", **kw):
        bar = super().add(child, text=text, **kw)
        for title, action in actions:
            action = tk.Button(bar, text=title, command=action)
            action.pack()
        return bar
