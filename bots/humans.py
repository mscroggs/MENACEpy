from .bot import Bot
from random import randrange

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
