import pygame
from scene import Scene

class Title(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.img_cursor = self.game.load_asset("cursor-4x7.png")
        self.selected = 0
        self.rows = 2
        self.selected_pos = [(0.03, 0.49), (0.2, 0.64)]
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((80, 120, 190))

        # write the title to the background
        text_title = self.game.make_text("4Jacks!", (30, 30, 30), 32)
        self.game.blit_centered(text_title, self.background, (.5, .2))

        text_hotseat = self.game.make_text("Play Multiplayer Locally", (50, 50, 50), 24)
        self.game.blit_centered(text_hotseat, self.background)

        text_ai = self.game.make_text("Play against AI", (50, 50, 50), 24)
        self.game.blit_centered(text_ai, self.background, (0.5, 0.65))

        self.game.blit_centered(surface=self.game.make_text(text="Q to Quit", color= (80, 80, 80), fontSize =30), target=self.background, position=(0.5, 0.8))

    def update(self):
        if pygame.K_SPACE in self.game.just_pressed or pygame.K_RETURN in self.game.just_pressed:
            if self.selected == 1:
                self.game.ai = 1  
            self.game.scene_replace = "GameBoard"
                
        if pygame.K_LEFT in self.game.just_pressed or pygame.K_UP in self.game.just_pressed:
            self.selected -= 1 
            self.selected %= self.rows
        if pygame.K_RIGHT in self.game.just_pressed or pygame.K_DOWN in self.game.just_pressed:
            self.selected += 1 
            self.selected %= self.rows


    def draw(self):
        if self.active: 
            self.screen.blit(self.background, (0, 0))
            self.game.blit_centered(
                self.img_cursor, self.screen, self.selected_pos[self.selected]
            )
        