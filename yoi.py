#!/usr/bin/env python3
import tkinter as tk
import time
import yoi

def main():
    start = time.perf_counter()
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Yoi")
    root.config(bg="#000")

    tabs = yoi.widgets.TabSystem(root)
    tab0 = yoi.widgets.Tab(tabs)
    tk.Label(tab0, text="tab0").pack()
    editor = yoi.widgets.Editor(tabs)
    tabs.open(tab0)
    tabs.open(editor)
    tabs.pack(fill="both", expand=True)

    return (time.perf_counter() - start, root)

if __name__ == "__main__":
    launchtime, rootwindow = main()
    print(f"launch time {launchtime:8.6f} sec")
    rootwindow.mainloop()
    yoi.util.cleanup(".")
