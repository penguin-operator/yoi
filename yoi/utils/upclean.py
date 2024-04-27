import os
import shutil

__all__ = ["upclean"]

def upclean(path: str):
    for root, dirs, files in os.walk(path):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            shutil.rmtree(pycache_path)
            dirs.remove('__pycache__')
