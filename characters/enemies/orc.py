from Characters.Enemies.Enemy import Enemy
class Orc(Enemy):
    def __init__(self, position, board):
        self.stats_attack = 3
        self.stats_defend = 2
        self.stats_body = 1
        self.stats_mind = 2
        self.stats_move = 8
        self.stats_weapon = "sword"
        self.stats_armour = None
        self.position = position
        self.tag = 'x'
        self.board = board
        self.board.update_position(position, position, self)

