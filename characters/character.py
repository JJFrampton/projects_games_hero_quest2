from actions.dice import Dice
from board.tiles.empty import Empty
import copy
class Character:
    d = Dice()
    movement = 0
    def __init__(self, position):
        print("initializing")
    def attack(self):
        print("attacking")
    def defend(self):
        print("defending")
        # this should be automatic response to being attacked
    def attack(self):
        return self.d.roll('w', self.stats_attack)
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
    # NOTE: this all might need to be moved into the board class
    #       need to check if move is possible first
    #       collision check (enemies, allies, walls, objects, boarders)
    #       OR
    #       change the order of checks, check board first
    def move_right(self, amount):
        if self.movement >= amount:
            new_position = self.position.copy()
            new_position[1] += amount
            moved = self.board.update_position(self, amount, 'right')
            if moved:
                self.position = new_position
                self.movement -= amount
                return True
            return False
        else:
            print("not enough moves")
            return False
        print("moving right")
    def move_left(self, amount):
        if self.movement >= amount:
            old_position = self.position.copy()
            self.movement -= amount
            self.position[1] -= amount
            new_position = self.position
            self.board.update_position(old_position, new_position, self)
            return True
        else:
            print("not enough moves")
            return False
        print("moving left")
    def move_up(self, amount):
        if self.movement >= amount:
            old_position = self.position.copy()
            self.movement -= amount
            self.position[0] -= amount
            new_position = self.position
            self.board.update_position(old_position, new_position, self)
            return True
        else:
            print("not enough moves")
            return False
        print("moving up")
    def move_down(self, amount):
        if self.movement >= amount:
            old_position = self.position.copy()
            self.movement -= amount
            self.position[0] += amount
            new_position = self.position
            self.board.update_position(old_position, new_position, self)
            return True
        else:
            print("not enough moves")
            return False
        print("moving down")

    def move(self, direction, amount):
        if self.movement < amount: return False
        result = self._collision_check(direction, amount)
        if result['collision']:
            print('collision')
            return False
        else:
            self._change_location(result['position'])
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
