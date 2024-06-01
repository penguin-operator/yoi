import tkinter as tk

def geometry_data(widget: tk.Widget) -> tuple[str, dict]:
    manager = widget.winfo_manager()
    data = {}
    if manager == "grid":
        data = widget.grid_info()
    elif manager == "pack":
        data = widget.pack_info()
    elif manager == "place":
        data = widget.place_info()
    return (manager, data)
