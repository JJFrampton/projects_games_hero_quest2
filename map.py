#!/usr/bin/env python3

# board details:
# horizontal_blocks = 26
# max_horizontal_walls = 10
# vertical_blocks = 19
# max_vertical_walls = 8

# game details:
# game will need blocks for the walls
# width = horizontal_blocks + max_horizontal_walls
# height = vertical_blocks + max_horizontal_walls

# horizontal_wall = '-'
# x = '-'
# vertical_wall = '|'
# y = '|'
# bottom_corner = '\''
# b = '\''
# top_corner = ','
# t = ','
# wall_joint = '+'
# j = '+'

# door = '#'
# d = '#'
# open_space = 'o'
# o = 'o'

# print("%s%s%s" %(top_corner, width-2, top_corner))

import csv

board = []
with open('hero_quest_board.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        board.append(row)
