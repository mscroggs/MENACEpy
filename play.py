#!/usr/bin/python
from __future__ import print_function

from menace import MENACE
from bots import Good
from game import Game

win,fail = 0,0

p1 = MENACE()
p2 = Good()

for i in range(100):
    g = Game(p1,p2)
    g.repeated_play(100)

    if sum(p1.boxes[0]) == 0:
        fail += 1
    else:
        win += 1

    p1.rebuild()

print(win,fail)
