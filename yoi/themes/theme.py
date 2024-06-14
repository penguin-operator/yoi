import tkinter as tk

class Theme:
    background = "#000"
    foreground = "#fff"
    borderwidth = 0
    highlightthickness = 0
    insertbackground = "#0f0"

    def __apply__(self, widget: tk.Misc):
        for option in filter(lambda x: not x.startswith("__"), self.__dir__()):
            if option in widget.keys():
                widget[option] = getattr(self, option)
        for child in widget.children.values():
            self.__apply__(child)
