import pygame
from scene import Scene
from gametoken import GameToken

class GameBoard(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.game.screen.fill((80, 80, 80))
        self.piece = GameToken(game)

        

    def update(self):
        if pygame.K_SPACE in self.game.just_pressed:
            self.game.scene_replace = "Title"
        self.piece.update()

    def draw(self):
        self.piece.draw()