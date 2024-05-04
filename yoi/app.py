import tkinter

import config
from utils import cleanup

class App(tkinter.Tk):
    def __init__(self, *, size="800x600"):
        super().__init__()

        x = int((self.winfo_screenwidth() - int(size.split('x')[0])) / 2)
        y = int((self.winfo_screenheight() - int(size.split('x')[1])) / 2)

        self.title("Yoi")
        self.geometry(f"{size}+{x}+{y}")

    def __del__(self):
        cleanup("yoi")
