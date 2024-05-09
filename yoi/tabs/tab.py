import tkinter as tk

class Tab(tk.Frame):
    def __init__(self):
        super().__init__(self.master)
        self.pack(fill="both", expand=1)
        self.bar = self.master.add(self, text=self.__class__.__name__)
