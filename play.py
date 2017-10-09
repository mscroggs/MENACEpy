#!/usr/bin/python
from __future__ import print_function

from bots import MENACE, Good
from game import Game

p1 = MENACE()
p2 = Good()

g = Game(p1,p2)
g.repeated_play(200)

p1.plot(show=True)
