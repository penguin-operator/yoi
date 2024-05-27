import tkinter as tk
from bars import Bar

class BarSystem(tk.Frame):
    __instance__ = None

    def __new__(cls, master):
        if not cls.__instance__:
            cls.__instance__ = tk.Frame.__new__(cls)
        Bar.master = cls.__instance__
        return cls.__instance__

    def __init__(self, master: tk.Misc):
        tk.Frame.__init__(self, master)
