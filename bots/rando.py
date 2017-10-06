from .bot import Bot
from random import randrange

class Rando(Bot):
    def __init__(self):
        self.name = "Rando Calrissian"

    def play(self, board):
        return randrange(9)
