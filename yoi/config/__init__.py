import sys
import os
import json
from types import ModuleType

jsontype = str | list | dict | int | float | bool | None

class Config(ModuleType):
    def __init__(self):
        super().__init__(__name__, __doc__)
        self.__path__: str = os.path.dirname(__file__)

    def __parse__(self, key: str) -> list[str | int]:
        return [int(k) if k.isdigit() else k for k in key.split('/')]

    def __getitem__(self, key: str) -> jsontype:
        file, *keys = self.__parse__(key)

        with open(os.path.join(self.__path__, file)) as f:
            data = json.load(f)

        for k in keys:
            try:
                data = data[k]
            except KeyError:
                raise KeyError(k)
        
        return data

    def __setitem__(self, key: str, value: jsontype):
        file, *keys = self.__parse__(key)

        with open(os.path.join(self.__path__, file)) as f:
            test = json.load(f)
            data = test.copy()

        for k in keys:
            try:
                test = test[k]
            except KeyError:
                raise KeyError(k)

        exec(f"data{"".join(
                f'[{k}]' if isinstance(k, int) else f'["{k}"]' for k in keys
            )} = value", {}, {
            "data": data,
            "value": value,
        })

        with open(os.path.join(self.__path__, file), 'w') as f:
            json.dump(data, f, indent=4)

sys.modules[__name__] = Config()
