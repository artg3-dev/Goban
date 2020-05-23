
"""
TODO:
- Switch validation to regex
- Handle metadata
- Handle branching
- Batch handling of moves
- Load sgf here instead of in gui
- OOP this stuff so you load an sgf into a parser object, then make it iterable
    * also alow for going backwards
"""









import re

class MoveSyntaxError(SyntaxError):
    def __init__(self):
        super().__init__('Invalid Move Syntax:')

COLORS = {'B':'b', 'W':'w'}
MOVES = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
       'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19}

def validate_move_syntax(move:str):
    move_regex = re.compile(r';[BW]\[[abcdefghijklmnopqrs]{2}\]', re.DOTALL)

    results = move_regex.search(move)
    if not results:
        raise MoveSyntaxError()
    else:
        return True

def get_meta(sgf:str):
    pass
    # sgf = sgf.replace('\n', '')


def parse_move(move:str):
    validate_move_syntax(move)
    color = move[1]
    x = MOVES[move[3]]
    y = MOVES[move[4]]
    return color, x, y


def test():
    print(parse_move(';B[dd]'))
    print(parse_move(';S[dd]'))

if __name__ == '__main__':
    test()
