import pygame
from scene import Scene


# A panel for displaying debug information/text within the game
class Debug(Scene):
    def __init__(self, game):
        super().__init__(game)

        # create a list of data to display
        self.data = []

        # make a transparent background
        self.background = self.game.make_transparent_surface(self.screen.get_size())

    def update(self):
        pass

    def draw(self):
        # prepend "Debug" to the data list then clear it after the draw
        self.data.insert(0, "Debug")

        # clear the previous text
        self.background.fill((0, 0, 0, 0))

        for i, data in enumerate(self.data):
            # update with the new text
            data = self.game.make_text(data, (30, 30, 30), 8)
            # draw the text to the top left of the background
            self.background.blit(data, (10, (i * 30) + 10))

        # clear the data list
        self.data = []

        # draw the background to the screen
        self.screen.blit(self.background, (0, 0))
