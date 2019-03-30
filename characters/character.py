from actions.dice import Dice
class Character:
    d = Dice()
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
