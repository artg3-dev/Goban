from tkinter import Tk
from tkinter import Button
from tkinter import Menu
from tkinter import Toplevel
from tkinter import Label
from tkinter import Entry
from tkinter import
from functools import partial # to allow button command with args
from goban_display import GobanDisplay

class EditMetaDialog:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.top.geometry("-600+100")
        self._create_components()

    def _create_components(self):
        Label(self.top, text="Value").grid(column=0, row=0)
        self.board_size = Entry(self.top)
        self.board_size = Entry(self.top)
        self.e.grid(column=1, row=0, padx=5)

        b = Button(self.top, text="OK", command=self.ok)
        b.grid(column=1, row=1, pady=5, fill=)

    def ok(self):
        self.text = self.e.get()
        self.top.destroy()

def main():
    root = Tk()
    display = GobanDisplay(root)
    display.pack()

    menu_bar = _create_menu_bar(root)
    root.config(menu=menu_bar)

    root.geometry("-300-50")
    root.mainloop()
    # button = Button(root, text='Press Me',
    #   command=partial(random_stone, display))
    # button.pack()

def _edit_metadata(root):
    dialog = EditMetaDialog(root)
    root.wait_window(dialog.top)
    print(dialog.text)


def donothing():
    print('nothing')

def _create_menu_bar(root):
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=donothing)
    file_menu.add_command(label="Save", command=donothing)
    file_menu.add_command(label="Save as...", command=donothing)
    file_menu.add_command(label="New Game", command=donothing)

    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Edit Metadata",
      command=partial(_edit_metadata, root))

    # Add to menu bar
    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    return menu_bar

if __name__ == '__main__':
    main()