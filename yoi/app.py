import tkinter

import config
import views
from utils import cleanup

class App(tkinter.Tk):
    def __init__(self, *, size="800x600"):
        super().__init__()
        self.title("Yoi")
        self.geometry(size)
        views.View(self).pack()

    def __del__(self):
        cleanup("yoi")
