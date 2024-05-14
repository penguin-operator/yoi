import os
import shutil
import tkinter as tk

def cleanup(path: str = "yoi"):
    for root, dirs, files in os.walk(path, topdown=False):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(root, "__pycache__"))

def keypad(widget: tk.Widget):
    kmap = {
        '<KP_Left>': '<Left>',
        '<KP_Right>': '<Right>',
        '<KP_Up>': '<Up>',
        '<KP_Down>': '<Down>',
        '<KP_Home>': '<Home>',
        '<KP_End>': '<End>',
        '<KP_Next>': '<Next>',
        '<KP_Prior>': '<Prior>',
        '<KP_Enter>': '<Return>',
    }

    for k in kmap:
        def handler(event, key=k):
            widget.event_generate(kmap[key], state=event.state)
        widget.bind(k, handler)
    return widget
