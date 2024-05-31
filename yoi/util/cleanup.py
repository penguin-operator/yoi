import os
import shutil

def cleanup(path: str):
    for root, dirs, _ in os.walk(path):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(root, "__pycache__"))
