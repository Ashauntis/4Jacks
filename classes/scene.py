class Scene:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.next = None
        self.quit = False
    
    def update(self):
        pass

    def draw(self):
        pass
