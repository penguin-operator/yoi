import tkinter as tk
from xml.dom import minidom

class SVGImage(tk.PhotoImage):
    """
    https://stackoverflow.com/questions/12284311/python-tkinter-how-to-work-with-pixels
    """
    def __init__(self, *, path: str = ...):
        tk.PhotoImage.__init__(self)
        self["width"] = 16
        self["height"] = 16
        for y in range(self.height()):
            for x in range(self.width()):
                self.put("#0f0", (x, y))
