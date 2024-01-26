import pygame
from scene import Scene
from gametoken import GameToken

class GameBoard(Scene):
    def __init__(self, game):
        super().__init__(game)

        
        self.piece = GameToken(game, "BLUE")
        self.key_color = (123, 231, 132) # some random garbage color
        self.board = pygame.Surface((400, 280)).convert()
        self.board.set_colorkey(self.key_color)     
        self.board.fill((33, 33, 255))

        for i in range(7):
            for j in range(6):
                print("drawing circle")
                pygame.draw.circle(self.board, self.key_color, (50 * i + 50, 40 * j + 40), 18)
            

    def update(self):
        if pygame.K_SPACE in self.game.just_pressed:
            self.game.scene_replace = "Title"
        if pygame.K_LEFT in self.game.just_pressed:
            pass
        if pygame.K_RIGHT in self.game.just_pressed: 
            pass
        self.piece.update()

    def draw(self):
        self.game.screen.fill((80, 80, 80))
        self.game.blit_centered(self.board, self.game.screen, (0.5, 0.56))
        self.piece.draw()