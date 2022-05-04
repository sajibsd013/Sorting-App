from tkinter import *
from GUI import app_gui


def main():
    # =======Main APP ======
    root = Tk()
    sa = app_gui.sorting_app(root)
    root.mainloop()


if __name__ == "__main__":
    main()
