from bots.bot import Bot
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
        self.start = [1,2,3,9]
        self.name = "MENACE"
        self.boxes = {}
        self.d_boxes = {}
        self.d_boxes[0] = new_box(Board(),self.start[3])
        self.data = [sum(self.d_boxes[0])]

        self.search_moves(Board())

        self.rebuild()

    def search_moves(self,board):
        played = 10 - board.count(0)
        move = 2 - played%2
        other = 3 - move
        minmove = 9
        for i in range(9):
            if board[i] == move:
                minmove = i
                break
        for i in range(minmove):
            if board[i]==0:
                newboard = board.copy()
                newboard[i] = move
                if move == 2:
                    if not newboard.has_winner() and newboard.is_max():
                        self.d_boxes[newboard.number()] = new_box(newboard,self.start[newboard.count(0)//2-1])
                if played < 7:
                    self.search_moves(newboard)

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
