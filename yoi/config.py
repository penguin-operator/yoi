import json
import sys
import os

class Config:
    def __init__(self, name: str):
        self.__name__ = name
        with open(f"~/.config/yoi/{name}.jsom", 'r') as data:
            self.data = json.load(data)

    def get(self, key, default=None):
        return self.data.get(key, default=default)

    def __getitem__(self, key):
        return self.data.__getitem__(key)

    def __setitem__(self, key, value):
        self.data[key] = value
        with open(f"~/.config/yoi/{self.__name__}.jsom", 'w') as data:
            self.data = json.dump(self.data, data)
    