import tkinter

class View(tkinter.Frame):
    def __init__(self, master: tkinter.Tk):
        super().__init__(master)
        self.master = master

    def title(self, title: str = "") -> str | None:
        return self.master.title(title)

    def __init_subclass__(cls, name: str):
        super().__init_subclass__()
