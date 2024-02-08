import game

class Game4Jacks(game.Game):
    def __init__(self):
        super().__init__()

        # set properties unique to the game
        self.ai = None
        
