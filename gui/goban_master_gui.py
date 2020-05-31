from tkinter import Tk
from tkinter import Button
from functools import partial # to allow button command with args

def main():

    root = Tk()

    display = GobanDisplay(root)
    display.pack()

    # button = Button(root, text='Press Me',
    #   command=partial(random_stone, display))
    # button.pack()

    root.geometry("-300-50")
    root.mainloop()

if __name__ == '__main__':
    main()