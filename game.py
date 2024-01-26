import os
import pygame
import settings
from scene import Scene
from scenes.title import Title
from scenes.gameboard import GameBoard


class Game:
    def __init__(self):
        # set the quit flag to false at the start
        self.quit = False
        self.pressed = []
        self.just_pressed = []
        self.__sfx = {}
        self.volume_music = 100
        self.volume_effects = 100

        # initialize pygame
        pygame.init()
        pygame.mixer.init()

        # load our sound effects
        for sound in settings.SFX_LIST:
            self.__sfx[sound] = pygame.mixer.Sound("assets/" + sound)

        # create a window
        self.screen = pygame.display.set_mode(
            settings.RESOLUTION, pygame.FULLSCREEN | pygame.SCALED
        )
        pygame.display.set_caption(settings.TITLE)

        # create a pygame clock to limit the game to 60 fps
        self.clock = pygame.time.Clock()

        # create a stack for scenes to be updated and drawn
        # and add the title scene to the stack
        self.scene = []  # type: list[Scene]
        self.scenes = settings.SCENE_LIST
        self.scene.append(self.load_scene(settings.SCENE_START))

        # create variables to handle scene changes
        self.scene_replace = None
        self.scene_push = None
        self.scene_pop = None

    def run(self):
        while not self.quit:
            # handle events and input
            self.get_events_and_input()

            # set all scenes to inactive except the top scene in the stack
            for scene in self.scene:
                scene.active = False
            self.scene[-1].active = True

            # process update for the top scene in the stack
            self.scene[-1].update()

            # draw all scenes in the stack from bottom to top
            for scene in self.scene:
                scene.draw()

            # update the display
            pygame.display.flip()

            # process scene change requests (if any)
            self.change_scenes()

            # limit the game to 60 fps
            self.clock.tick(settings.FPS)

    def get_events_and_input(self):
        # get input
        self.pressed = pygame.key.get_pressed()
        self.just_pressed = []

        # get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                self.just_pressed.append(event.key)

        # check for escape key to quit
        if pygame.K_ESCAPE in self.just_pressed:
            self.scene_pop = True
            # self.quit = True

    def load_asset(self, asset_path: str):
        return pygame.image.load("assets/" + asset_path).convert_alpha()

    def change_scenes(self):
        # check for scene changes
        if self.scene_replace is not None:
            if self.scene_replace in self.scenes:
                self.scene = []
                self.scene.append(self.load_scene(self.scene_replace))
            self.scene_replace = None

        elif self.scene_push is not None:
            if self.scene_push in self.scenes:
                self.scene.append(self.load_scene(self.scene_push))
            self.scene_push = None

        elif self.scene_pop is not None:
            if len(self.scene) > 1:
                self.scene.pop()
            else:
                print("WARNING: Cannot pop last scene! Exiting!")
                self.quit = True
            self.scene_pop = None

    def load_scene(self, scene: str):
        print("load_scene: " + scene)
        if scene in self.scenes:
            # use an eval to return the scene based on the scene string
            return eval(scene + "(self)")
        else:
            return Title(self)

    # from the pygame tutorial:
    # https://www.pygame.org/docs/tut/tom_games3.html
    def load_png(self, name):
        """Load image and return image object"""
        fullname = os.path.join("assets", name)
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
        if font is None:
            font = "assets/" + settings.FONT

        return pygame.font.Font(font, fontSize).render(text, 1, color)

    def make_transparent_surface(self, size):
        return pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()

    def blit_centered(self, surface, target, position=(0.5, 0.5)):
        """
        This function places a given surface at a specified position on the target surface.

        Parameters:
        Surface (pygame.Surface): The surface to be placed. This is a pygame Surface object, which can be
        created using pygame.font.Font.render() method.

        target (pygame.Surface): The target surface on which the surface is to be placed. This could be
        the game screen or any other surface.

        position (tuple): A tuple of two values between 0 and 1, representing the relative position
        on the target surface where the surface should be placed. The values correspond to the horizontal
        and vertical position respectively. For example, a position of (0.5, 0.5) will place the text dead
        center on the target surface.


        """
        surface_position = surface.get_rect()
        surface_position.centerx = target.get_rect().centerx * position[0] * 2
        surface_position.centery = target.get_rect().centery * position[1] * 2
        target.blit(surface, surface_position)

    def play_sound(self, sound):
        # set the volume of the sound based on the settings
        self.__sfx[sound].set_volume(self.volume_effects / 100)

        pygame.mixer.Sound.play(self.__sfx[sound])
