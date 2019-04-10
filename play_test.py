from board.board import Board
from board.tiles.empty import Empty
from board.tiles.wall import Wall
from board.tiles.tile import Tile
from characters.players.elf import Elf

board = Board()

p1 = Elf('yoshida', [2,3], board)
p2 = Elf('dayoshi', [3,6], board)
