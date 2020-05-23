from tkinter import Canvas
from tkinter import Frame
from tkinter import BOTH






"""
TODO:
- Separate the game board into a class, separate from the gui display!
    * Store moves 1 by 1 in list for moving forward and backwards
- Add coordinates (big yikes)
- Move sgf loading into the parser
"""










class GobanDisplay(Frame):
    COLORS = {'B':'Black', 'W':'White'}

    def __init__(self, master, height=608, width=608):
        Frame.__init__(self, master)
        self.grid()

        self.canvas = Canvas(self, bg='#FFE15C', height=height, width=height)

        # _div is the division factor for grid spacing
        self.hdiv = height / 20
        self.wdiv = width / 20

        # Draw Grid
        for i in range(19):
            # Vertical Line
            x = (i * self.wdiv) + self.wdiv # add wdiv to get off of the edge by 1 square
            y1 = self.hdiv
            y2 = height - self.hdiv
            self.canvas.create_line(x, y1, x, y2)

            # Horizontal Line
            y = (i * self.hdiv) + self.hdiv
            x1 = self.wdiv
            x2 = (width - self.wdiv) + 1 # +1 to overlap on the edge
            self.canvas.create_line(x1, y, x2, y)

        # Marker Coords
        markers = [
            # Corners
            (4, 4), (16, 16), (4, 16), (16, 4),
            # Sides
            (10, 4), (4, 10), (16, 10), (10, 16),
            # Tengen
            (10, 10)
        ]

        # Draw Marking Circles
        for x, y in markers:
            ox1 = (x * self.wdiv) - int(self.wdiv/4) + 4
            oy1 = (y * self.hdiv) - int(self.hdiv/4) + 4
            ox2 = (x * self.wdiv) + int(self.wdiv/4) - 4
            oy2 = (y * self.hdiv) + int(self.hdiv/4) - 4
            self.canvas.create_oval(ox1, oy1, ox2, oy2,
              outline='Black', fill='Black')

        self.canvas.pack(fill=BOTH, padx=5, pady=5)

    def place_stone(self, color:str, x:int, y:int):
        # Verify valid color input
        if color not in list(self.COLORS.keys()):
            print(color)
            raise ValueError('Player color not valid')
        else:
            stone_color = self.COLORS[color]

        # +/- 1 are for shrinking the stone by 2 pixels from grid width
        ox1 = (x * self.wdiv) - int(self.wdiv/2) + 1
        oy1 = (y * self.hdiv) - int(self.hdiv/2) + 1
        ox2 = (x * self.wdiv) + int(self.wdiv/2) - 1
        oy2 = (y * self.hdiv) + int(self.hdiv/2) - 1

        self.canvas.create_oval(ox1, oy1, ox2, oy2, outline=stone_color, fill=stone_color)

    def load_sgf_from_text(self, sgf_text):
        import sgf_tools.sgf_parser as parser
        moves = sgf_text.split('\n')
        for move in moves:
            color, x, y = parser.parse_move(move)
            self.place_stone(color, x, y)

def main():
    # Testing purposes only
    from tkinter import Tk
    from tkinter import Button
    from functools import partial # to allow button command with args

    root = Tk()

    display = GobanDisplay(root)
    display.pack()

    button = Button(root, text='Press Me',
      command=partial(random_stone, display))
    button.pack()

    root.geometry("-300-50")
    root.mainloop()

# Testing only
def random_stone(display):
    # from random import randint
    # x = randint(1, 19)
    # y = randint(1, 19)
    # try:
    #     if display.stone_color == 'W':
    #         display.stone_color = 'B'
    #     else:
    #         display.stone_color = 'W'
    # except AttributeError:
    #     display.stone_color = 'B'
    #
    # display.place_stone(display.stone_color, x, y)
    with open('sgf info.sgf') as f:
        text = f.read()
    display.load_sgf_from_text(text)


if __name__ == '__main__':
    main()
