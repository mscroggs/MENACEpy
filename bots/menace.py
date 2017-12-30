from .bot import Bot
from game import Board
from random import randrange, choice
from itertools import permutations

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

class MENACE(Bot):
    def __init__(self):
        start = [1,2,3,9]
        self.name = "MENACE"
        self.boxes = {}
        self.d_boxes = {}
        self.d_boxes[0] = new_box(Board(),start[3])
        self.data = [sum(self.d_boxes[0])]

        for i,j in permutations(range(9),2):
            board = Board()
            board[i] = 1
            board[j] = 2
            if board.number() not in self.d_boxes and board.is_max() and not board.has_winner():
                self.d_boxes[board.number()] = new_box(board,start[2])

        for i,j,k,l in permutations(range(9),4):
            board = Board()
            board[i] = 1
            board[j] = 2
            board[k] = 1
            board[l] = 2
            if board.number() not in self.d_boxes and board.is_max() and not board.has_winner():
                self.d_boxes[board.number()] = new_box(board,start[1])

        for i,j,k,l,m,n in permutations(range(9),6):
            board = Board()
            board[i] = 1
            board[j] = 2
            board[k] = 1
            board[l] = 2
            board[m] = 1
            board[n] = 2
            if board.number() not in self.d_boxes and board.is_max() and not board.has_winner():
                self.d_boxes[board.number()] = new_box(board,start[0])

        assert len(self.d_boxes) == 304

        self.rebuild()

    def rebuild(self):
        self.boxes = {}
        for a,b in self.d_boxes.items():
            self.boxes[a] = [i for i in b]

    def play(self, board):
        if board.count(0) == 1:
            for i,j in enumerate(board):
                if j==0:
                    return i
        n,rot = board.max_number_and_rotations()
        rot = choice(rot)
        box = self.boxes[n]
        if sum(box) == 0:
            return "RESIGN"
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
        self.add_data_point()

    def lose(self):
        for n,i in self.used:
            self.boxes[n][i] -= 1
        self.add_data_point()

    def draw(self):
        for n,i in self.used:
            self.boxes[n][i] += 1
        self.add_data_point()

    def add_data_point(self):
        self.data.append(sum(self.boxes[0]))

    def plot(self, filename=None, show=None):
        import matplotlib.pylab as plt
        plt.plot(range(len(self.data)),self.data,"ko")
        plt.xlabel("Number of games")
        plt.ylabel("Change in number of beads in first box")
        if filename is not None:
            plt.savefig(filename)
        if show:
            plt.show()
        plt.clf()
