import os
import pygame
from classes.scenes.title import Title
from classes.scenes.gameboard import GameBoard
from settings import RESOLUTION, FPS

class Game():
    def __init__(self):


        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.quit = False
        self.scene = Title(self)
        self.scenes = ['Title', 'GameBoard']
        self.pressed = []
        self.just_pressed = []

    def run(self):
        while not self.quit:
            self.handle_input()

            self.scene.update()
            self.scene.draw()

            if self.scene.quit:
                self.quit = True

            if self.scene.next is not None:
                print('Switching to scene: ' + self.scene.next)
                if self.scene.next in self.scenes:
                    self.scene = eval(self.scene.next + '(self)')   # eval() is evil but it works

            pygame.display.flip()
            self.clock.tick(FPS)

    def handle_input(self):
        self.pressed = pygame.key.get_pressed()
        self.just_pressed = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                self.just_pressed.append(event.key)

    def load_png(name):
        """ Load image and return image object"""
        fullname = os.path.join("data", name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except FileNotFoundError:
            print(f"Cannot load image: {fullname}")
            raise SystemExit
        return image, image.get_rect()
        

    def make_text(self, text, color, fontSize, font=None):
        return pygame.font.Font(font, fontSize).render(text, 1, color)

    def place_text_absolute(self, text, target, position):
        target.blit(text, position)

    def place_text_centered(self, text, target, position):
        textpos = text.get_rect()
        textpos.centerx = target.get_rect().centerx * position[0]
        textpos.centery = target.get_rect().centery * position[1]
        target.blit(text, textpos)
