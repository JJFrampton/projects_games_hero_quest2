from Resources.Board import Board
b = Board(4,4)
from Characters.Players.Elf import Elf
p1 = Elf("yoshi", [0,0], b)
print(b.map)
p1.turn_start()
p1.movement_roll()
print(p1.movement)
p1.move_right(1)
print(b.map)
