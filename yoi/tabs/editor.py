import tkinter as tk
from .tab import Tab

class Editor(Tab):
    def __init__(self):
        Tab.__init__(self)
        self.title("Editor")
        self.editor = tk.Text(self)
        self.editor.pack(fill="both", expand=True)
