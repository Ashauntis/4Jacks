import pygame
from scene import Scene

class Title(Scene):
    def __init__(self, game):
        super().__init__(game)
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((80, 120, 190))

        # write the title to the background
        text_title = self.game.make_text("4Jacks!", (30, 30, 30), 64)
        self.game.blit_centered(text_title, self.background, (.5, .2))

        text_start = self.game.make_text("Press Enter to Start", (50, 50, 50), 48)
        self.game.blit_centered(text_start, self.background)

        self.game.blit_centered(surface=self.game.make_text(text="Q to Quit", color= (80, 80, 80), fontSize =30), target=self.background, position=(1, 1.5))

    def update(self):
        if pygame.K_SPACE in self.game.just_pressed:
            self.game.scene_replace = "GameBoard"

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        