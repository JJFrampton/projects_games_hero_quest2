from .content import StaticTile
class Wall(StaticTile):
    def __init__(self, display):
        self.name = 'wall'
        super().__init__(display)
