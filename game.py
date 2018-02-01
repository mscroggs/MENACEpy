from __future__ import print_function
from exceptions import *

def board_n(board):
    out = 0
    for a in range(9):
        out += 3**a * board[a]
    return out

class Board(object):
    def __init__(self, board=None):
        if board is None:
            self.pieces = [0]*9
            self.reset()
        else:
            self.pieces = [i for i in board.pieces]
        self.rotations = [(0,1,2,3,4,5,6,7,8),
                          (6,3,0,7,4,1,8,5,2),
                          (8,7,6,5,4,3,2,1,0),
                          (2,5,8,1,4,7,0,3,6),
                          (2,1,0,5,4,3,8,7,6),
                          (0,3,6,1,4,7,2,5,8),
                          (6,7,8,3,4,5,0,1,2),
                          (8,5,2,7,4,1,6,3,0)]

    def copy(self):
        return Board(self)

    def number(self):
        return board_n(self.pieces)

    def max_number(self):
        return self.max_number_and_rotations()[0]

    def max_rotations(self):
        return self.max_number_and_rotations()[1]

    def is_max(self):
        return self.max_number() == self.number()

    def max_number_and_rotations(self):
        out = [-1,[]]
        for r in self.rotations:
            this = board_n([self[i] for i in r])
            if this > out[0]:
                out = [this,[]]
            if this == out[0]:
                out[1].append(r)
        return out

    def winner(self):
        for a,b,c in [(0,1,2),(3,4,5),(6,7,8),
                      (0,3,6),(1,4,7),(2,5,8),
                      (0,4,8),(2,4,6)]:
            if self[a] != 0 and self[a] == self[b] == self[c]:
                return self[a]
        if 0 not in self.pieces:
            return 0
        return None

    def has_winner(self):
        if self.winner() is None:
            return False
        return True

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
        self.resigned = None

    def next_move(self):
        if self.move % 2 == 0:
            p = self.p1
        else:
            p = self.p2
        pos = None
        while pos != "RESIGN" and (pos is None or self.board[pos] != 0):
            pos = p.play(self.board)
        if pos == "RESIGN":
            self.resigned = 1 + self.move % 2
        else:
            self.board[pos] = 1 + self.move % 2
            self.move += 1

    def winner(self):
        if self.resigned is not None:
            return 3-self.resigned
        return self.board.winner()

    def play(self, printing=False):
        self.reset()
        while self.winner() is None:
            self.next_move()
        w = self.winner()
        if w == 0:
            self.p1.draw()
            self.p2.draw()
            if printing:
                print("Draw")
        if w == 1:
            self.p1.win()
            self.p2.lose()
            if printing:
                print(self.p1.name,"wins")
        if w == 2:
            self.p1.lose()
            self.p2.win()
            if printing:
                print(self.p2.name,"wins")
        return self.winner()

    def repeated_play(self, n, printing=False):
        games = []
        for i in range(n):
            games.append(self.play(printing))

        print(games.count(0),"draws")
        print(games.count(1),self.p1.name,"wins")
        print(games.count(2),self.p2.name,"wins")
