#!/usr/bin/python
from __future__ import print_function

from bots import Rando, Good
from game import Game

p1 = Rando()
p2 = Good()

g = Game(p1,p2)
g.repeated_play(10000)
