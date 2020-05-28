from tkinter import Canvas
from tkinter import Frame
from tkinter import BOTH
from tkinter import Event
from math import ceil
from math import floor

from gamerules.kifu_tracker import KifuTracker




"""
TODO:
- Separate the game board into a class, separate from the gui display!
    * Clean up methods that double up on checking move validity (add_move)
- Move sgf loading into the parser
"""










class GobanDisplay(Frame):
    COLORS = {'B':'Black', 'W':'White'}

    def __init__(self, master,
      sq_width=30, sq_height=30, h_pad=50, w_pad=50,
      board_color='#FFE15C', marking_color='#373737'):
        Frame.__init__(self, master)
        self.grid()

        # Colors
        self.board_color = board_color
        self.marking_color = marking_color

        # Dimensions of the goban
        self.sq_width = sq_width
        self.sq_height = sq_height
        self.h_pad = h_pad
        self.w_pad = w_pad
        self.width = (18 * self.sq_width) + (19) + (2 * self.h_pad)
        self.height = (18 * self.sq_height) + (19) + (2 * self.w_pad)

        # Stored information for use by methods
        self.tracker = KifuTracker()
        self.stones = {}
        self.highlighted = None
        self.highlighted_move = None
        self._move_color = 'B'

        self.canvas = Canvas(self, bg=self.board_color,
          height=self.height, width=self.height, cursor='none')
        self.canvas.bind('<Motion>', self._highlight)
        self.canvas.bind('<Button-1>', self.add_move)

        self._add_grid()
        self._add_markers()
        self._add_grid_labels()

        self.canvas.pack(fill=BOTH, padx=5, pady=5)


    def add_move(self, event:Event):
        color, x, y = self.highlighted_move
        if self.tracker.space_is_open(self.highlighted_move[1], # [1] = x ...
          self.highlighted_move[2]):
            # Add move/stone to all relevant datasets
            self.tracker.add_move(self.highlighted_move)
            stone = self._place_stone(color, x, y)
            self.stones[self.highlighted_move] = stone

            # Remove highlighting effect
            self.canvas.delete(self.highlighted)
            self.highlighted = None
            self.highlighted_move = None

            if self._move_color == 'B':
                self._move_color = 'W'
            else:
                self._move_color = 'B'

    def _highlight(self, event:Event, color='#00E218'):
        x, y = self._get_nearest(event.x, event.y)
        self.canvas.delete(self.highlighted)
        if (x >= 0 and x < 19) and (y >= 0 and y < 19):
            self.highlighted = self._draw_circle(x+1, y+1, 14.5,
              outline_color=color, fill_color=None, thickness=2)
            self.highlighted_move = (self._move_color, x + 1, y + 1)
        else:
            self.highlighted_move = None

    def _get_nearest(self, x, y):
        nearest_y = round((y - self.h_pad) / self.sq_height)
        nearest_x = round((x - self.w_pad) / self.sq_width)
        return nearest_x, nearest_y

    def _get_pixel(self, x, y):
        # Convert from go numbering to python numbering
        x -= 1
        y -= 1

        x_coord = (self.h_pad + 1) + (x * (self.sq_width + 1))
        y_coord = (self.w_pad + 1) + (y * (self.sq_height + 1))
        return x_coord, y_coord

    def _add_grid(self):
        for i in range(1, 20):
            # Vertical Line
            x, y1 = self._get_pixel(i, 1)
            _, y2 = self._get_pixel(i, 19)
            self.canvas.create_line(x, y1, x, y2 + 1, fill=self.marking_color)  # +1 for overlap

            # Horizontal Line
            x1, y = self._get_pixel(1, i)
            x2, _ = self._get_pixel(19, i)
            self.canvas.create_line(x1, y, x2, y, fill=self.marking_color)

    def _add_markers(self):
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
            self._draw_circle(x, y, 3, self.marking_color, self.marking_color)

    def _add_grid_labels(self):
        offset = 25
        labels = list('ABCDEFGHJKLMNOPQRST')

        for i, char in enumerate(labels):
            i += 1 # Convert from py numbering to go numbering

            # Left
            _, y = self._get_pixel(0, i)
            x = self.h_pad - offset
            self.canvas.create_text(x, y, text=str(20 - i),
              fill=self.marking_color)

            # Right
            x = (self.width - self.h_pad) + offset
            self.canvas.create_text(x, y, text=str(20 - i),
              fill=self.marking_color)

            # Top
            x, _ = self._get_pixel(i, 0)
            y = self.w_pad - offset
            self.canvas.create_text(x, y, text=char,
              fill=self.marking_color)

            # Top
            y = (self.height - self.w_pad) + offset
            self.canvas.create_text(x, y, text=char,
              fill=self.marking_color)

    def _draw_circle(self, x, y, r, outline_color, fill_color, thickness=1):
        x_center, y_center = self._get_pixel(x, y)
        x1 = x_center - r
        y1 = y_center - r
        x2 = x_center + r
        y2 = y_center + r

        return self.canvas.create_oval(x1, y1, x2, y2,
          outline=outline_color, fill=fill_color, width=thickness)

    def _place_stone(self, color:str, x:int, y:int, stone_size=14.5):
        try:
            stone_color = self.COLORS[color]
        except KeyError:
            raise KeyError("Invalid Stone Color: Use either 'B' or 'W'")

        return self._draw_circle(x, y, stone_size, stone_color, stone_color)

    # Testing method to be removed
    def load_sgf_from_text(self, sgf_text):
        import sgf_tools.sgf_parser as parser
        moves = sgf_text.split('\n')
        for move in moves:
            color, x, y = parser.parse_move(move)
            self._place_stone(color, x, y)

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
