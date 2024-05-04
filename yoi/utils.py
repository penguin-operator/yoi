import os
import shutil

def cleanup(path: str = "yoi"):
    for root, dirs, files in os.walk(path, topdown=False):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(root, "__pycache__"))
