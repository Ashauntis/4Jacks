import pygame
# 640x360 7x6 board
class GameToken():
    def __init__(self, game):
        self.game = game
        
        # create a transparent surface for the token to be drawn upon
        self.sprite = self.game.make_transparent_surface((32, 32))
        
        pygame.draw.circle(self.sprite, "RED", (16, 16), 16)
        
    def update(self):
        if pygame.K_SPACE in self.game.just_pressed:
                pygame.draw.circle(self.sprite, "GREEN", (16, 16), 16)

    def draw(self):
        self.game.screen.blit(self.sprite, (0, 0))