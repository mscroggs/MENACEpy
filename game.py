from __future__ import print_function
from exceptions import *

class Board(object):
    def __init__(self):
        self.reset()

    def count(self,n):
        return self.pieces.count(n)

    def __iter__(self):
        return self.pieces.__iter__()

    def __str__(self):
        return "\n".join(["".join([[" ","o","x"][i] for i in self.pieces[j:j+3]]) for j in range(0,9,3)])

    def __unicode__(self):
        return self.__str__()

    def reset(self):
        self.pieces = [0]*9

    def winner(self):
        for a,b,c in [(0,1,2),(3,4,5),(6,7,8),
                      (0,3,6),(1,4,7),(2,5,8),
                      (0,4,8),(2,4,6)]:
            if self[a] != 0 and self[a] == self[b] == self[c]:
                return self[a]
        if 0 not in self.pieces:
            return 0
        return None

    def __getitem__(self, n):
        return self.pieces[n]

    def __setitem__(self, n, p):
        if self.pieces[n] == 0:
            self.pieces[n] = p
        else:
            raise InvalidMove


class Game(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p1.turn = 1
        self.p2 = p2
        self.p2.turn = 2
        self.board = Board()
        self.reset()

    def reset(self):
        self.board.reset()
        self.p1.reset()
        self.p2.reset()
        self.move = 0

    def next_move(self):
        if self.move % 2 == 0:
            p = self.p1
        else:
            p = self.p2
        pos = None
        while pos is None or self.board[pos] != 0:
            pos = p.play(self.board)
        self.board[pos] = 1 + self.move % 2
        self.move += 1

    def play(self):
        self.reset()
        while self.board.winner() is None:
            self.next_move()
        w = self.board.winner()
        if w == 0:
            self.p1.draw()
            self.p2.draw()
        if w == 1:
            self.p1.win()
            self.p2.lose()
        if w == 2:
            self.p1.lose()
            self.p2.win()
        return self.board.winner()

    def repeated_play(self, n):
        games = []
        for i in range(n):
            games.append(self.play())

        print(games.count(0),"draws")
        print(games.count(1),self.p1.name,"wins")
        print(games.count(2),self.p2.name,"wins")
