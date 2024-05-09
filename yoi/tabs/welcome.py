import tkinter as tk
from .tab import Tab

class Welcome(Tab):
    def __init__(self):
        super().__init__()
        # self.title("Welcome")
        self.welcome = tk.Label(self, text="Welcome to Yoi", font=("Fira Code", 40))
        self.welcome.pack(side="top", pady=32)
