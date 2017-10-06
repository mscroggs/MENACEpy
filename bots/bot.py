class Bot(object):
    def __init__(self):
        self.name = "Nameless bot"

    def play(self, board):
        raise NotImplementedError

    def reset(self):
        pass

    def win(self):
        pass

    def lose(self):
        pass

    def draw(self):
        pass
