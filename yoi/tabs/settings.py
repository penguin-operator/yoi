from .tab import Tab

class Settings(Tab):
    def __init__(self):
        super().__init__()
        self.title("Settings")
        self["bg"] = "#f0f"
