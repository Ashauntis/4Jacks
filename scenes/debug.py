import pygame
from scene import Scene

# A panel for displaying debug information/text within the game
class Debug(Scene):
    def __init__(self, game):
        super().__init__(game)
        
        # create a list of data to display
        self.data = ["Debug:",]

        # make a transparent background
        self.background = self.game.make_transparent_surface(self.screen.get_size())
        
    def update(self):
        # update the background with the new text
        for i, data in enumerate(self.data):
            # clear the previous text
            self.background.fill((0, 0, 0, 0))
            # update with the new text
            data = self.game.make_text(data, (30, 30, 30), 8)
            # draw the text to the top left of the background
            self.background.blit(data, (10, (i * 30) + 10))

    def draw(self):
        # draw the background to the screen
        self.screen.blit(self.background, (0, 0))
