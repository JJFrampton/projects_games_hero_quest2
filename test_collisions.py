import numpy as np
def p(m):
    print(np.matrix(m.map))

from Resources.Board import Board
b = Board(4,4)
from Characters.Players.Elf import Elf
p1 = Elf("yoshi", [1,1], b)
from Characters.Enemies.Orc import Orc
p2 = Orc([0,1], b)

print(np.matrix(b.map))
p1.turn_start()
p1.movement_roll()
print(p1.movement)
p1.move_up(1)
print(np.matrix(b.map))
