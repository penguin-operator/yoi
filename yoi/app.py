import time
import tkinter as tk
from utils import *
from widgets import *
from tabs import *
from bars import *

class App(tk.Tk):
    __start__ = time.perf_counter()

    def __init__(self, *, size="1280x720"):
        tk.Tk.__init__(self)
        x = int((self.winfo_screenwidth() - int(size.split('x')[0])) / 2)
        y = int((self.winfo_screenheight() - int(size.split('x')[1])) / 2)
        self.title("Yoi")
        self.geometry(f"{size}+{x}+{y}")

        self.bars = BarSystem(self)
        self.tabs = TabSystem(self)
        self.bars.pack(side="left", fill="y")
        self.tabs.pack(side="top", fill="both", expand=1)
        self.statusbar = tk.Frame(self, height=20)
        self.statusbar.pack(side="bottom", fill='x')

        Welcome()
        Editor()

    def launchtime(self):
        print(f"launchtime: {time.perf_counter() - self.__start__}")

    def __del__(self):
        cleanup("yoi")
