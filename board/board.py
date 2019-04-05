import numpy as np
# used for __init__
from board.tiles.empty import Empty
from board.tiles.wall import Wall
from board.tiles.tile import Tile

class Board:
    # def __init__(self,y,x):
    def __init__(self):
        # self.m = [ ['o'] * x for i in range(y) ]
        # self.m = np.array(self.m)
        # print(m)

        e = Empty('o')
        m = []
        for y in range(6):
            xarr = []
            for x in range(10):
                xarr.append(Tile(e))
            m.append(xarr)

        v = Wall('|')
        h = Wall('-')
        tc = Wall(',')
        bc = Wall('\'')
        for i in range(10):
            if i < 6:
                m[i][0].content = v
                m[i][9].content = v
            m[0][i].content = h
            m[5][i].content = h
        m[5][0].content = h
        m[0][0].content = tc
        m[0][9].content = tc
        m[5][0].content = bc
        m[5][9].content = bc

        # elf = Elf('yoshida', [1,1], m)

        print("HORIZONTALLY SPACED BOARD")
        for y in range(len(m)):
            for x in range(len(m[y])):
                print("%s " % m[y][x].content.display, end='')
            print('')
        print('\n')

        print(isinstance(m[1][1], Tile))
        print(isinstance(m[1][1].content, Empty))
        print(isinstance(m[0][0].content, Wall))

        self.m = m



    def display(self):
        m = self.m
        for y in range(len(m)):
            for x in range(len(m[y])):
                print("%s " % m[y][x].content.display, end='')
            print('')
        print('\n')
    def init_position(self, character):
        y = character.position[0]
        x = character.position[1]
        print(x)
        print(y)
        # self.m[y,x] = character.tag
        # should be a movement service
        character.previous_content = self.m[y][x].content
        self.m[y][x].content = character
        print(isinstance(character.previous_content, Empty))
    def update_position(self, character, amount, direction):
        old_position = character.position
        if amount == 0:
            y = old_position[0]
            x = old_position[1]
            self.m[y,x] = character.tag
            return True
        if not self.collision(old_position, amount, direction):
            y = old_position[0]
            x = old_position[1]
            self.m[y,x] = 'o'
            y = new_position[0]
            x = new_position[1]
            self.m[y,x] = character.tag
            return True
        return False

    # SHOULD BE USING A METHOD LIKE THIS THROUGHOUT
    def get_tile(self, position):
        return self.m[ position[0] ][ position[1] ]
    def get_content(self, position):
        return self.m[ position[0] ][ position[1] ].content

    def collision(self, old, amount, direction):
        # print('old')
        # print(old)
        # print('new')
        # print(new)
        # only one dir at a time

        # y = new[0] - old[0]
        # x = new[1] - old[1]

        # path = self.m[old[0]:new[0]+1, old[1]:new[1]+1]
        # path = np.array(path)
        # path = path.flatten()
        # unique = set(path)
        # print(unique)
        # print(unique == {'o'})

        if direction == 'left':
            path = self.m[old[0]:old[0]+1, old[1]+1:old[1]+amount+1]
        if direction == 'right':
            path = self.m[old[0]:old[0]+1, old[1]+amount:old[1]]
        if direction == 'up':
            path = self.m[old[0]+amount:old[0], old[1]:old[1]+1]
        if direction == 'down':
            path = self.m[old[0]+1:old[0]+amount+1, old[1]:old[1]+1]

        path = path.flatten()
        if set(path) == {'o'}:
            return False

        return True


# board = [
#         ['o','o','o','o'],
#         ['o','o','o','o'],
#         ['o','o','o','o'],
#         ['o','o','o','o']
#       ]
