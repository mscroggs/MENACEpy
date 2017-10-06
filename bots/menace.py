from .bot import Bot
from random import randrange, choice
from itertools import permutations

def board_n(board):
    out = 0
    for a in range(9):
        out += 3**a * board[a]
    return out

def new_box(board, n):
    out = [n]*9
    for i,j in enumerate(board):
        if j != 0:
            out[i] = 0
    rs = board.max_rotations()
    if len(rs) > 1:
        for i,j in enumerate(out):
            if j!=0:
                for r in rs:
                    if i != r[i]:
                        out[r[i]] = 0
    return out

class MBoard(object):
    def __init__(self, board=None):
        if board is None:
            self.pieces = [0]*9
        else:
            self.pieces = board.pieces
        self.rotations = [(0,1,2,3,4,5,6,7,8),
                          (6,3,0,7,4,1,8,5,2),
                          (8,7,6,5,4,3,2,1,0),
                          (2,5,8,1,4,7,0,3,6),
                          (2,1,0,5,4,3,8,7,6),
                          (0,3,6,1,4,7,2,5,8),
                          (6,7,8,3,4,5,0,1,2),
                          (8,5,2,7,4,1,6,3,0)]

    def __getitem__(self, n):
        return self.pieces[n]

    def __iter__(self):
        return self.pieces.__iter__()

    def __setitem__(self, n, p):
        self.pieces[n] = p

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

class MENACE(Bot):
    def __init__(self):
        self.name = "MENACE"
        self.boxes = {}
        self.boxes[0] = new_box(MBoard(),4)

        for i,j in permutations(range(9),2):
            board = MBoard()
            board[i] = 1
            board[j] = 2
            if board.number() not in self.boxes and board.is_max() and not board.has_winner():
                self.boxes[board.number()] = new_box(board,3)

        for i,j,k,l in permutations(range(9),4):
            board = MBoard()
            board[i] = 1
            board[j] = 2
            board[k] = 1
            board[l] = 2
            if board.number() not in self.boxes and board.is_max() and not board.has_winner():
                self.boxes[board.number()] = new_box(board,2)

        for i,j,k,l,m,n in permutations(range(9),6):
            board = MBoard()
            board[i] = 1
            board[j] = 2
            board[k] = 1
            board[l] = 2
            board[m] = 1
            board[n] = 2
            if board.number() not in self.boxes and board.is_max() and not board.has_winner():
                self.boxes[board.number()] = new_box(board,1)

        assert len(self.boxes) == 304

    def play(self, board):
        if board.count(0) == 1:
            for i,j in enumerate(board):
                if j==0:
                    return i
        mb = MBoard(board)
        n,rot = mb.max_number_and_rotations()
        rot = choice(rot)
        box = self.boxes[n]
        bead = randrange(sum(box))
        N = 0
        for i,j in enumerate(box):
            N += j
            if bead < N:
                self.used.append((n,i))
                return rot[i]

    def reset(self):
        self.used = []

    def win(self):
        for n,i in self.used:
            self.boxes[n][i] += 3

    def lose(self):
        for n,i in self.used:
            self.boxes[n][i] -= 1

    def draw(self):
        for n,i in self.used:
            self.boxes[n][i] += 1

