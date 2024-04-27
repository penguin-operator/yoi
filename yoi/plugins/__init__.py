import os

for root, dirs, files in os.walk(os.path.dirname(__file__)):
    for file in files:
        if file.endswith(".py"):
            __import__(f"yoi.plugins.{file[:-3]}")
