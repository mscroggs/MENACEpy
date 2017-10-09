from .bot import Bot
from random import randrange,choice

class QuiteGood(Bot):
    def __init__(self):
        self.name = "Quite Good Human"

    def play(self, board):
        for piece in [self.turn, 3-self.turn]:
            for a,b,c in [(0,1,2),(3,4,5),(6,7,8),
                          (0,3,6),(1,4,7),(2,5,8),
                          (0,4,8),(2,4,6)]:
                for x,y,z in [(a,b,c),(b,c,a),(c,a,b)]:
                    if board[x] == board[y] == piece and board[z] == 0:
                        return z
        return randrange(9)

class Good(Bot):
    def __init__(self):
        self.name = "Perfect Human"

    def play(self, board):
        rotations = board.rotations
        for piece in [self.turn, 3-self.turn]:
            for a,b,c in [(0,1,2),(3,4,5),(6,7,8),
                          (0,3,6),(1,4,7),(2,5,8),
                          (0,4,8),(2,4,6)]:
                for x,y,z in [(a,b,c),(b,c,a),(c,a,b)]:
                    if board[x] == board[y] == piece and board[z] == 0:
                        return z

        # FIRST o MOVE
        if board.count(0) == 9:
            return 0

        # SECOND o MOVE
        if board.count(0) == 7:
            if board[4] == 0:
                return 4
            return 8

        # FIRST x MOVE
        if board.count(0) == 8:
            if board[4] == 0:
                return 4
            return 0

        # SECOND x MOVE
        if board.count(0) == 6:
            for r in board.rotations:
                if board[r[0]] == board[r[8]] == 1:
                    return r[1]
                if board[r[1]] == board[r[3]] == 1:
                    return r[0]
                if board[r[4]] == board[r[8]] == 1 and board[r[0]] == 2:
                    return r[2]
                if board[r[3]] == board[r[5]] == 1 and board[r[4]] == 2:
                    return r[1]
                if board[r[3]] == board[r[8]] == 1 and board[r[4]] == 2:
                    return r[7]

        # THIRD x MOVE
        if board.count(0) == 4:
            for r in board.rotations:
                if board[r[0]] == board[r[6]] == board[r[5]] == 1 and board[r[3]] == board[r[4]] == 2:
                    return r[1]
                if board[r[0]] == board[r[7]] == board[r[5]] == 1 and board[r[3]] == board[r[4]] == 2:
                    return r[2]
                if board[r[1]] == board[r[7]] == board[r[5]] == 1 and board[r[3]] == board[r[4]] == 2:
                    return r[0]
                if board[r[1]] == board[r[3]] == board[r[8]] == 1 and board[r[0]] == board[r[4]] == 2:
                    return r[6]
                if board[r[1]] == board[r[4]] == board[r[8]] == 1 and board[r[0]] == board[r[7]] == 2:
                    return r[3]


        # 012
        # 345
        # 678

        if board.count(0) > 2:
            print(board)

        return choice([i for i,j in enumerate(board) if j==0])
