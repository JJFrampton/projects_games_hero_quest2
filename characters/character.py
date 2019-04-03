from actions.dice import Dice
from board.tiles.empty import Empty
import copy
# NOTES:
# make a better get method for the board
# should only have to pass the position array
# the board object can look up the tile
class Character:
    d = Dice()
    movement = 0
    def __init__(self, position):
        print("initializing")
    def attack(self, direction):
        print("attacking", direction)
        target = self._increment(direction, self.position)
        target = self.board.m[target[0]][target[1]]
        if type(target.content) == Empty:
            print('target is empty')
        else:
            print('you hit something')
    def defend(self):
        print("defending")
        # this should be automatic response to being attacked
    def defend(self):
        return self.d.roll('w', self.stats_defend)
    def turn_start(self):
        # set booleans
        self.movement = 0
        self.moved = False
        self.actioned = False
        print("Start turn")
    def turn_end(self):
        # wipe out unused movement
        self.movement = 0
        print("End turn")

    # movement
    def move(self, direction, amount):
        if self.movement < amount: return False
        result = self._collision_check(direction, amount)
        if result['collision']:
            print('collision')
            return False
        else:
            self._change_location(result['position'])
            self.movement -= amount
            return True

    def _increment(self, direction, position):
        if direction == 'R':
            position[1] += 1
            return position
        if direction == 'L':
            position[1] -= 1
            return position
        if direction == 'U':
            position[0] -= 1
            return position
        if direction == 'D':
            position[0] += 1
            return position

    def _collision_check(self, direction, amount):
        collision = {}
        position_to_check = copy.copy(self.position)
        for i in range(amount):
            position_to_check = self._increment(direction, position_to_check)
            tile = self.board.m[ position_to_check[0] ][ position_to_check[1] ]
            if not self._tile_free(tile):
                collision['collision'] = True
                collision['position'] = position_to_check
                return collision

        print(position_to_check)
        collision['collision'] = False
        collision['position'] = position_to_check
        return collision

    def _tile_free(self, tile):
        if tile.content.display != 'o':
            return False
        return True

    def _change_location(self, new_position):
        print('changing location')
        print(self.board.m[self.position[0]][self.position[1]].content)
        print(self.position[0])
        print(self.position[1])
        self.board.m[self.position[0]][self.position[1]].content = Empty('o')
        self.board.m[new_position[0]][new_position[1]].content = self
        self.position = new_position
