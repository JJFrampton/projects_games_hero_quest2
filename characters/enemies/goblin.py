from Characters.Enemies.Enemy import Enemy
class Goblin(Enemy):
    def __init__(self, position):
        self.stats_attack = 2
        self.stats_defend = 1
        self.stats_body = 1
        self.stats_mind = 1
        self.stats_move = 10
        self.stats_weapon = "sword"
        self.stats_armour = None
        self.position = position

