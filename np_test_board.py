#!/usr/bin/env python3
import pandas as pd

# NOTE not a production implimentation

board = pd.read_csv('hero_quest_board.csv', header=None)
board = board.replace('x','-')
board = board.replace('y','|')
board = board.replace('t',',')
board = board.replace('b','\'')
board = board.replace('j','+')
board = board.replace('o',' ')
print()
print("PANDAS BOARD")
print(board)
print("NOTES:")
print("might be too spaced out, difficult to tell where gaps are")

board = board.to_numpy()

print()
print("NORMAL BOARD")
for y in range(len(board)):
    for x in range(len(board[y])):
        print(board[y][x], end='')
    print('')
print("NOTES:")
print("best option, programatically")

print()
print("HORIZONTALLY SPACED BOARD")
for y in range(len(board)):
    for x in range(len(board[y])):
        print("%s " % board[y][x], end='')
    print('')
print("NOTES:")
print("no issues with counting spaces as this is just for printing")
