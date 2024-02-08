import pygame
from scene import Scene


class GameOver(Scene):
    def __init__(self, game):
        super().__init__(game)

        # colors for the game
        self.colors = ["RED", "YELLOW"]

        # make a transparent background
        self.background = self.game.make_transparent_surface(self.screen.get_size())

        # create the text
        text_game_over = self.game.make_text("Game Over!", (0, 0, 0), 8 * 8)
        if self.game.winner == 2:
            text_winner = self.game.make_text("T I E !", (0, 0, 0), 8 * 8)
        else:
            text_winner = self.game.make_text(
                self.colors[self.game.winner] + " WINS",
                self.colors[self.game.winner],
                8 * 3,
            )

        # write the text to the background
        self.game.blit_centered(text_game_over, self.background, (0.51, 0.5))
        self.game.blit_centered(text_winner, self.background, (0.5, 0.15))

    def update(self):
        if (
            pygame.K_SPACE in self.game.just_pressed
            or pygame.K_ESCAPE in self.game.just_pressed
        ):
            self.game.winner = None
            self.game.scene_pop = 2

    def draw(self):
        # draw the background to the screen
        self.screen.blit(self.background, (0, 0))
