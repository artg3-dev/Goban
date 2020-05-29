# Actually manages the keeping track of moves and removing captured stones
from collections import deque









"""
TODO:
- Move goban into it's own class for readability
- Disallow self-capture moves

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
        self.captures = {'B':0, 'W':0}
        self.board = [['-' for i in range(19)] for i in range(19)]

    def space_is_open(self, x, y):
        return self.board[x - 1][y - 1] == '-'

    def get_move(self, x, y):
        if self.board[x-1][y-1] != '-':
            return self.board[x-1][y-1], x, y
        else:
            return None

    def add_move(self, move:tuple):
        color, x, y = move
        if self.space_is_open(move[1], move[2]): # [1] = x ...
            self.board[x - 1][y - 1] = color

            move_group = self.get_connected_group(move)
            captures = self._get_removals(move)

            # Check for suicidal move
            if self.count_liberties(move_group) == 0 and not captures:
                self.board[x - 1][y - 1] = '-'
                raise InvalidMoveError(1)
            else: # If move is valid
                self.move_history.append(move)
                if captures:
                    for stone in captures:
                        self._remove_stone(stone)
                return captures
        else:
            raise InvalidMoveError(0)

    def _remove_stone(self, move:tuple):
        color, x, y = move
        self.board[x - 1][y - 1] = '-'
        self.captures[color] += 1

    def _get_removals(self, move):
        # Get all neighboring groups
        removals = []
        neighbors = self._get_neighbor_stones(move)
        n_groups = [self.get_connected_group(m) for m in neighbors]
        for group in n_groups:
            if group[0][0] == move[0]: # Won't check group of same color
                continue
            if self.count_liberties(group) == 0:
                for stone in group:
                    removals.append(stone)

        return tuple(removals)


    def _get_neighbor_stones(self, move):
        neighbors = []
        for x, y in self._get_possible_neighbors(move):
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
        open_spaces = set()
        for stone in group:
            for n in self._get_possible_neighbors(stone):
                if self.space_is_open(n[0], n[1]):
                    open_spaces.add(n)

        return len(open_spaces)

    def __str__(self):
        row_strings = []
        for row in self.board:
            row_strings.append(' '.join(row))

        return '\n'.join(row_strings)

    @staticmethod
    def _get_possible_neighbors(move):
        color, move_x, move_y = move
        possible_coords = [
            (move_x - 1, move_y),
            (move_x + 1, move_y),
            (move_x, move_y - 1),
            (move_x, move_y + 1)
        ]

        possible_neighbors = []
        for mv in possible_coords:
            x, y = mv
            if x > 0 and x <= 19 and y > 0 and y <= 19:
                possible_neighbors.append(mv)

        return(tuple(possible_neighbors))







# Testing methods
def add_testing_moves(tracker:KifuTracker):
    move_1 = ('B', 10, 10)
    move_2 = ('W', 9, 10)
    move_3 = ('W', 11, 10)
    move_4 = ('W', 10, 9)
    move_5 = ('W', 10, 11)
    move_6 = ('W', 7, 10)
    tracker.add_move(move_1)
    # print(tracker.get_connected_group(move_1))
    tracker.add_move(move_2)
    # print(tracker.get_connected_group(move_2))
    tracker.add_move(move_3)
    # print(tracker.get_connected_group(move_3))
    tracker.add_move(move_4)
    # print(tracker.get_connected_group(move_4))
    tracker.add_move(move_5)
    # print(tracker.get_connected_group(move_5))
    # tracker.add_move(move_6)
    # print(tracker.get_connected_group(move_6))
    # group = tracker.get_connected_group(move_2)
    # libs = tracker.count_liberties(group)

    # print(f'Liberties: {libs}')
    print(tracker)
    print(tracker.captures)
    print(tracker.move_history)

def main():
    tracker = KifuTracker()
    add_testing_moves(tracker)

if __name__ == '__main__':
    main()





