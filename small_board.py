from board.board import Board
from board.tiles.empty import Empty
from board.tiles.wall import Wall
from board.tiles.tile import Tile
from characters.players.elf import Elf

board = Board()

p1 = Elf('yoshida', [1,1], board)

# e = Empty('o')
# map = []
# for y in range(6):
#     xarr = []
#     for x in range(10):
#         xarr.append(Tile(e))
#     map.append(xarr)

# v = Wall('|')
# h = Wall('-')
# tc = Wall(',')
# bc = Wall('\'')
# for i in range(10):
#     if i < 6:
#         map[i][0].content = v
#         map[i][9].content = v
#     map[0][i].content = h
#     map[5][i].content = h
# map[5][0].content = h
# map[0][0].content = tc
# map[0][9].content = tc
# map[5][0].content = bc
# map[5][9].content = bc

# # elf = Elf('yoshida', [1,1], map)

# print("HORIZONTALLY SPACED BOARD")
# for y in range(len(map)):
#     for x in range(len(map[y])):
#         print("%s " % map[y][x].content.display, end='')
#     print('')
# print('\n')

# print(isinstance(map[1][1], Tile))
# print(isinstance(map[1][1].content, Empty))
# print(isinstance(map[0][0].content, Wall))


