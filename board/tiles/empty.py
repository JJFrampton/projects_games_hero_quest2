from .content import StaticTile
class Empty(StaticTile):
    def __init__(self, display):
        self.name = 'empty'
        super().__init__(display)
