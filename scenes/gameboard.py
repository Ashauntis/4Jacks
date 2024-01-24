import pygame
from scene import Scene

class GameBoard(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        if pygame.K_SPACE in self.game.just_pressed:
            self.game.scene_replace = "Title"

    def draw(self):
        self.game.screen.fill((255, 0, 255))