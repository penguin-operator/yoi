#!/usr/bin/env python3
import tkinter as tk
import time
import yoi

def main():
    root = tk.Tk()
    root.geometry("800x600+0+0")
    root.title("Yoi")

    tabs = yoi.widgets.TabSystem(root)
    welcome = yoi.widgets.Welcome(tabs)
    editor = yoi.widgets.Editor(tabs)
    tabs.open(welcome)
    tabs.add(editor)
    tabs.pack(fill="both", expand=True)

    yoi.themes.Theme().__apply__(root)

    return root

if __name__ == "__main__":
    start = time.perf_counter()
    rootwindow = main()
    print(f"launch time {time.perf_counter() - start:8.6f} sec")
    rootwindow.mainloop()
    yoi.util.cleanup(".")
