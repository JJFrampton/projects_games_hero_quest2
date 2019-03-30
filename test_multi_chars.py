import numpy as np
def p(m):
    print(np.matrix(m.map))

from Resources.Board import Board
b = Board(4,4)
from Characters.Players.Elf import Elf
p1 = Elf("yoshi", [0,0], b)
from Characters.Enemies.Orc import Orc
p2 = Orc([3,3], b)

print(np.matrix(b.map))
p1.turn_start()
p1.movement_roll()
print(p1.movement)
p1.move_right(1)
print(np.matrix(b.map))
