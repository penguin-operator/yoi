import tkinter
import config
from utils import cleanup

class App:
    def __init__(self, master=None, *, size="800x600"):
        self.master = master if master else tkinter.Tk()
        self.master.title("Yoi")
        self.master.geometry(size)
        self.master.protocol("WM_DELETE_WINDOW", self.destroy)

    def title(self, title: str = "") -> str | None:
        return self.master.title(title)

    def mainloop(self):
        self.master.mainloop()

    def destroy(self):
        self.master.destroy()
        cleanup("yoi")
