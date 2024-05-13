import tkinter as tk
from .tab import Tab

class Welcome(Tab):
    def __init__(self):
        Tab.__init__(self)
        self.title("Welcome!")
        self.welcome = tk.Label(self, text="Welcome to Yoi", font=("Fira Code", 50))
        self.welcome.pack(side="top", pady=1)
