import tkinter

class View(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__bar__ = tkinter.Frame(master)
