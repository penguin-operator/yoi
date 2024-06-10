import tkinter as tk
from yoi.util.font_tuple import font_tuple
from yoi.widgets.tab import Tab
from yoi.widgets.tabsystem import TabSystem

class Welcome(Tab):
    def __init__(self, master: TabSystem, cnf={}, **kw):
        Tab.__init__(self, master, cnf, **kw)
        font = font_tuple(master.option_get("font", "TkDefaultFont"))[0]
        tk.Label(self, text="Yoi", font=(font, 40)).pack(pady=60)
