import json
import sys
import os
from types import ModuleType

path = lambda name: os.path.join(os.path.dirname(__file__), name)

class Settings(ModuleType):
    def __init__(self):
        super().__init__("settings", __doc__)

    def __parse__(self, key: str) -> list[str | int | float]:
        return [ k for k in key.split('/') ]

    def __getitem__(self, key: str) -> dict | list | int | float | bool | str | None:
        return json.load(open(path(f"{key}.json")))

sys.modules[__file__] = Settings()
