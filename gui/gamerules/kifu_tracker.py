# Actually manages the keeping track of moves and removing captured stones
from collections import deque









"""
TODO:
- Keep track of captured stones for each color


"""


class InvalidMoveError(Exception):
    def __init__(self, error_type:int):
        error_types = {
            0:'Space is already occupied',
            1:'Move is self suicide',
            2:"Invalid Color: Use either 'B' or 'W'"
        }
        self.error_type = 'Invalid Move - ' + error_types.get(error_type,
          'Unspecified')
        super().__init__(self.error_type)

class KifuTracker(object):
    def __init__(self):
        self.move_history = deque()
        self.b_captures = 0
        self.w_captures = 0
        self.board = [['-' for i in range(19)] for i in range(19)]

    def space_is_open(self, move):
        return self.board[move[1]-1][move[2]-1] == '-'

    def get_move(self, x, y):
        if self.board[x-1][y-1] != '-':
            return self.board[x-1][y-1], x, y
        else:
            return None

    def add_move(self, move:tuple):
        color, x, y = move
        if self.space_is_open(move):
            self.board[x - 1][y - 1] = color
            self.move_history.append(move)
            return self._get_removals(move)
        else:
            raise InvalidMoveError(0)

    def _get_removals(self, move):
        # Setup
        checked_moves = set()
        to_check = set()
        to_check.add(move)

    def _get_neighbor_stones(self, move):
        color, move_x, move_y = move
        neighbors = []
        possible_neighbors = [
            (move_x - 1, move_y),
            (move_x + 1, move_y),
            (move_x, move_y - 1),
            (move_x, move_y + 1)
        ]

        for x, y in possible_neighbors:
            if x < 1 or x > 19 or y < 1 or y > 19:
                continue
            else:
                move = self.get_move(x, y)
                if move:
                    neighbors.append(move)

        return tuple(neighbors)

    def get_connected_group(self, move):
        # Setup
        group_color = move[0]
        group = [move]
        neighbors = self._get_neighbor_stones(move)
        to_check = set(neighbors)
        checked = set()
        checked.add(move) # move is already added to group

        while to_check:
            # Retrieve random move to check
            a_move = to_check.pop()
            if a_move[0] == group_color:
                group.append(a_move)
                checked.add(a_move)
                # Get a_move's neighbors and add to the to_check if not already
                # checked
                for m in self._get_neighbor_stones(a_move):
                    if m not in checked:
                        to_check.add(m)
            else:
                checked.add(a_move)

        return tuple(group)

    def count_liberties(self, group:tuple):
        # Psudo code:
        # liberties = set()
        # for stone in group:
            # liberties.add(neighbor == empty)
        # return len(liberties)
        pass

    def __str__(self):
        row_strings = []
        for row in self.board:
            row_strings.append(' '.join(row))

        return '\n'.join(row_strings)


def add_testing_moves(tracker:KifuTracker):
    move_1 = ('B', 10, 10)
    move_2 = ('W', 9, 10)
    move_3 = ('W', 9, 11)
    move_4 = ('W', 8, 10)
    move_5 = ('W', 8, 11)
    move_6 = ('W', 7, 9)
    tracker.add_move(move_1)
    print(tracker.get_connected_group(move_1))
    tracker.add_move(move_2)
    print(tracker.get_connected_group(move_2))
    tracker.add_move(move_3)
    print(tracker.get_connected_group(move_3))
    tracker.add_move(move_4)
    print(tracker.get_connected_group(move_4))
    tracker.add_move(move_5)
    print(tracker.get_connected_group(move_5))
    tracker.add_move(move_6)
    print(tracker.get_connected_group(move_6))

def main():
    tracker = KifuTracker()
    add_testing_moves(tracker)
    print(tracker)

if __name__ == '__main__':
    main()