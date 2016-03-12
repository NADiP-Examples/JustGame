from tkinter import *
from tkinter.filedialog import *


class OpenDialog():
    def __init__(self):
        self.value = False

    def open(self, l):
        self.root = Tk()
        self.value = askopenfile().name
        self.root.mainloop()


def opening(a):
    root = Tk()
    op = askopenfile()

    root.mainloop()


def new(a):
    root = Tk()
