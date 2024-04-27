import os
import sys

from app import Yoi

def main():
    if os.fork() == 0:
        yoi = Yoi()
        yoi(*sys.argv[1:])

if __name__ == "__main__":
    main()
