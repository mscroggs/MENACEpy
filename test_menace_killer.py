#!/usr/bin/python
from __future__ import print_function

from menace import MENACE
from bots import MenaceKiller, Good
from game import Game

win,fail = 0,0

print("Against perfect")
p1 = MENACE()
p2 = Good()

g = Game(p1,p2)
g.repeated_play(1000)

print("Against MENACE killer")
p1 = MENACE()
p2 = MenaceKiller()

g = Game(p1,p2)
g.repeated_play(1000)

#p1.plot(show=True)
