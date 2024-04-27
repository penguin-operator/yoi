import os
import sys
import tkinter

import utils
import views
import themes
import plugins
import settings

class Yoi:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("yoi")
        self.root.config(background="#000")

    def __call__(self, *args: str):
        self.root.mainloop()

    def __del__(self):
        utils.upclean.upclean(os.path.dirname(__file__))

    def restart(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

    def exit(self):
        self.root.destroy()

    def title(self, title: str = "") -> str | None:
        return self.root.title(title)
