import tkinter as tk

class Bar(tk.Frame):
    __instance__ = None

    def __new__(cls, master):
        if not cls.__instance__:
            cls.__instance__ = tk.Frame.__new__(cls)
        return cls.__instance__
