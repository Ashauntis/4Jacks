import pygame
from scene import Scene


class GameOver(Scene):
    def __init__(self, game):
        super().__init__(game)

        # make a transparent background
        self.background = self.game.make_transparent_surface(self.screen.get_size())

        # create the text
        text_title = self.game.make_text("Game Over!", (30, 30, 30), 32)
        text_start = self.game.make_text(self.game.winner, (50, 50, 50), 24)

        # write the text to the background
        self.game.blit_centered(text_title, self.background, (0.5, 0.2))
        self.game.blit_centered(text_start, self.background)

    def update(self):
        if pygame.K_SPACE in self.game.just_pressed:
            self.game.winner = None
            self.game.scene_replace = "GameBoard"

    def draw(self):
        # draw the background to the screen
        self.screen.blit(self.background, (0, 0))
