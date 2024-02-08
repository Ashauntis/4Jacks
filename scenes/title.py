import pygame
from scene import Scene
import random


class Title(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.img_cursor = self.game.load_asset("cursor-4x7.png")
        self.positions = [(0.03, 0.49), (0.2, 0.64), (0.2, 0.74)]
        
        self.selected_position = 0
        self.selected_ai_color = 1
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((80, 120, 190))

        # write the title to the background
        text_title = self.game.make_text("4Jacks!", (30, 30, 30), 32)

        # generate the text to write the background
        text_hotseat = self.game.make_text("Play Multiplayer Locally", (50, 50, 50), 24)
        text_ai = self.game.make_text("Play against AI", (50, 50, 50), 24)
        text_quit = self.game.make_text(text="Esc/Q to Quit", color= (80, 80, 80), fontSize =24)

        # generate the ai text that
        self.text_ai_color = []
        self.text_ai_color.append(self.game.make_text("AI Color: Red   ", (50, 50, 50), 16))
        self.text_ai_color.append(self.game.make_text("AI Color: Yellow", (50, 50, 50), 16))
        self.text_ai_color.append(self.game.make_text("AI Color: Random", (50, 50, 50), 16))


        # write the static text to the background
        self.game.blit_centered(text_title, self.background,  (.5, .2))
        self.game.blit_centered(text_hotseat, self.background)
        self.game.blit_centered(text_ai, self.background, (0.5, 0.65))
        self.game.blit_centered(text_quit, self.background, (0.5, 0.8))

    def update(self):
        if pygame.K_SPACE in self.game.just_pressed or pygame.K_RETURN in self.game.just_pressed:
            # starting at the top option, start the game in hotseat mode
            if self.selected_position == 0:
                self.game.ai = None
                self.game.scene_push = "GameBoard"

            # if the user selects the second option, set the game to hotseat mode and start it
            if self.selected_position == 1:
                if self.selected_ai_color == 2:
                    self.game.ai = random.choice([0, 1])
                else:
                    self.game.ai = self.game.selected_ai_color
                self.game.scene_push = "GameBoard"

            # if the user selects the third option, change the AI color setting
            if self.selected_position == 2:
                self.selected_ai_color += 1
                self.selected_ai_color %= len(self.text_ai_color)
                
        if pygame.K_LEFT in self.game.just_pressed or pygame.K_UP in self.game.just_pressed:
            self.selected_position -= 1 
            self.selected_position %= len(self.positions)
        if pygame.K_RIGHT in self.game.just_pressed or pygame.K_DOWN in self.game.just_pressed:
            self.selected_position += 1 
            self.selected_position %= len(self.positions)


    def draw(self):
        if self.active:
            # draw the background 
            self.screen.blit(self.background, (0, 0))

            # draw the dynamic text for ai color to the screen
            self.game.blit_centered(
                self.text_ai_color[self.selected_ai_color], self.screen, (.5, .74)
            )

            # draw the cursor
            self.game.blit_centered(
                self.img_cursor, self.screen, self.positions[self.selected_position]
            )
        