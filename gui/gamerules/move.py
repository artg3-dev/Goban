class Move(object):
    def __init__(self, color, x, y):
        if color != 'B' or color != 'W':
            raise InvalidMoveError(2)
        self.color = color
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Move):
            if self.color != other.color:
                return False
            elif self.x != other.x:
                return False
            elif self.y != other.y:
                return False
            else:
                return True
        return False

    def __str__(self):
        return f'{self.color}: ({self.x}, {self.y})'