import tkinter as tk

class Tab(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, self.master.space)
        self.master = self.master.master
        self.__button__ = tk.Button(self.master.titlebar, text=self.__class__.__name__, command=self.select)
        self.__button__.pack(side="left")
        self.__actions__ = tk.Frame(self.master.titlebar)
        self.__actions__.pack(side="right")
        self.master.add(self)

    def title(self, title: str = "") -> str | None:
        if title:
            self.__button__["text"] = title
        else:
            return self.__button__["text"]

    def select(self):
        self.master.select(self)

    def close(self):
        self.master.close(self)
