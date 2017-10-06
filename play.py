#!/usr/bin/python
from __future__ import print_function

from bots import MENACE, QuiteGood
from game import Game

p1 = MENACE()
p2 = QuiteGood()

g = Game(p1,p2)
g.repeated_play(1000)
