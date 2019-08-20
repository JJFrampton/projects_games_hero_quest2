from actions.dice import Dice
from board.tiles.empty import Empty
import copy
# NOTES:
# make a better get method for the board
# should only have to pass the position array
# the board object can look up the tile
class Character:
    dice = Dice()
    movement = 0
    def __init__(self, position):
        print("initializing")
    def attack(self, direction):
        """This is a test of documentation.

            All methods should have this for documentation
            for more examples (ie, modules, classes, etc):
            https://www.pythonforbeginners.com/basics/python-docstrings
        """
        print("attacking", direction)
        #get target
        target = self._increment(direction, copy.copy(self.position))
        target = self.board.m[target[0]][target[1]]
        target = target.content
        if type(target) == Empty:
            print('target is empty')
        else:
            print('you hit something')
            target.defend(self.attack_roll())
            # get attack power from self
            # get defense from target.content
    def attack_roll(self):
        return self.dice.roll('w', self.stats_attack)['white_skull']
    def defend(self, attack_to_defend):
        print("defending")
        defense = self.dice.roll('w', self.stats_defend)['shield']

        print("attack : ", attack_to_defend )
        print("defense : ", defense )

        damage = attack_to_defend - defense
        if damage > 0:
            self.stats_body -= damage
            if self.stats_body < 1:
                self.die()
    def die(self):
        print('You died')
        del self
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
        if self.moved: return False
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
