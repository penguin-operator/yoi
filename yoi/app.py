import tkinter as tk
from utils import cleanup
from tabs import Tabs, Tab, Welcome, Settings

class App(tk.Tk):
    def __init__(self, *, size="1400x800"):
        super().__init__()
        x = int((self.winfo_screenwidth() - int(size.split('x')[0])) / 2)
        y = int((self.winfo_screenheight() - int(size.split('x')[1])) / 2)
        self.title("Yoi")
        self.geometry(f"{size}+{x}+{y}")

        self.tabs = Tabs(self)
        self.tabs.pack(side="top", fill="both", expand=1)
        self.statusbar = tk.Frame(self, height=20, bg="#fff")
        self.statusbar.pack(side="bottom", fill='x')

        Settings()
        Welcome()

    def __del__(self):
        cleanup("yoi")
