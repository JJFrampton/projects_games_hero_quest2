from characters.character import Character
class Player(Character):
    def movement_roll(self):
        Character.moved = True
        self.movement = Character.dice.roll('r', self.stats_move)
