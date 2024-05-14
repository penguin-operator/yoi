import json

class Config:
    def __init__(self, name: str):
        self.__name__ = name
        self.__file__ = open(f"~/.yoi/config/{name}.jsom", 'r')
        self.__data__ = json.load(self.__file__)

    def __getitem__(self, key):
        return self.__data__.__getitem__(key)

    def __setitem__(self, key, value):
        self.__data__[key] = value
        json.dump(self.__data__, self.__file__)
    
    def __del__(self):
        self.__file__.close()

    def get(self, key, default=None):
        return self.__data__.get(key, default=default)

    def keys(self):
        return self.__data__.keys()

    def values(self):
        return self.__data__.values()

    def items(self):
        return self.__data__.items()
