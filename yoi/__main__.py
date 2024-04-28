import os
from app import App

def main():
    app = App()

    if os.fork() == 0:
        app.mainloop()

if __name__ == "__main__":
    main()
