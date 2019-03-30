import numpy as np
class Board:
    def __init__(self,y,x):
        self.map = [ ['o'] * x for i in range(y) ]
        self.map = np.array(self.map)
        print(map)
    def init_position(self, character):
        y = character.position[0]
        x = character.position[1]
        self.map[y,x] = character.tag
    def update_position(self, character, amount, direction):
        old_position = character.position
        if amount == 0:
            y = old_position[0]
            x = old_position[1]
            self.map[y,x] = character.tag
            return True
        if not self.collision(old_position, amount, direction):
            y = old_position[0]
            x = old_position[1]
            self.map[y,x] = 'o'
            y = new_position[0]
            x = new_position[1]
            self.map[y,x] = character.tag
            return True
        return False
    def collision(self, old, amount, direction):
        # print('old')
        # print(old)
        # print('new')
        # print(new)
        # only one dir at a time

        # y = new[0] - old[0]
        # x = new[1] - old[1]

        # path = self.map[old[0]:new[0]+1, old[1]:new[1]+1]
        # path = np.array(path)
        # path = path.flatten()
        # unique = set(path)
        # print(unique)
        # print(unique == {'o'})

        if direction == 'left':
            path = self.map[old[0]:old[0]+1, old[1]+1:old[1]+amount+1]
        if direction == 'right':
            path = self.map[old[0]:old[0]+1, old[1]+amount:old[1]]
        if direction == 'up':
            path = self.map[old[0]+amount:old[0], old[1]:old[1]+1]
        if direction == 'down':
            path = self.map[old[0]+1:old[0]+amount+1, old[1]:old[1]+1]

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
