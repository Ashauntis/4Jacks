import time
import math
import pygame


class Scene:
    def __init__(self, game):
        self.game = game
        self.active = True
        self.screen = game.screen
        self.start = time.time()
        self.shadow_intensity = 100
        self.shadow_depth = 3

    def elapsed(self):
        return time.time() - self.start

    def constrain(self, n, n_min, n_max):
        return max(min(n_max, n), n_min)

    def update(self):
        print("Scene's update method has not been implemented")

    def draw(self):
        # the values of sin range from -1 to 1
        r = math.sin(time.time() * 1.33 + 1.5) * 127 + 128
        g = math.sin(time.time()) * 127 + 128
        b = math.sin(time.time() * 0.25 - 0.6666) * 127 + 128
        self.screen.fill((r, g, b))
        print("Scene's draw method has not been implemented")

    def draw_box(self, position: tuple, size: tuple):
        if self.elapsed() < self.box_delay:
            # expand the box from it's center to it's full size
            position = (
                position[0] + size[0] / 2 * (1 - self.elapsed() / self.box_delay),
                position[1] + size[1] / 2 * (1 - self.elapsed() / self.box_delay),
            )

            size = (
                size[0] * self.elapsed() / self.box_delay,
                size[1] * self.elapsed() / self.box_delay,
            )

            # draw the blue background
            pygame.draw.rect(
                self.game.screen,
                (0, 0, 255),
                (position[0], position[1], size[0], size[1]),
                width=0,
            )

            # draw the white border
            pygame.draw.rect(
                self.game.screen,
                (255, 255, 255),
                (position[0], position[1], size[0], size[1]),
                width=2,
            )
            return

        # create a drop shadow for the box

        for i in range(1, self.shadow_depth + 1):
            self.draw_rect_alpha(
                self.game.screen,
                (0, 0, 0, self.shadow_intensity),
                (position[0] + i, position[1] + i, size[0], size[1]),
            )

        # draw the blue background
        pygame.draw.rect(
            self.game.screen,
            (0, 0, 255),
            (position[0], position[1], size[0], size[1]),
            width=0,
        )

        # draw the white border
        pygame.draw.rect(
            self.game.screen,
            (255, 255, 255),
            (position[0], position[1], size[0], size[1]),
            width=2,
        )

    def draw_box_centered(self, position: tuple, size: tuple):
        if self.elapsed() < self.box_delay:
            # expand the box from it's center to it's full size

            size = (
                size[0] * self.elapsed() / self.box_delay,
                size[1] * self.elapsed() / self.box_delay,
            )

            # draw the blue background
            pygame.draw.rect(
                self.game.screen,
                (0, 0, 255),
                (
                    position[0] - size[0] / 2,
                    position[1] - size[1] / 2,
                    size[0],
                    size[1],
                ),
                width=0,
            )

            # draw the white border
            pygame.draw.rect(
                self.game.screen,
                (255, 255, 255),
                (
                    position[0] - size[0] / 2,
                    position[1] - size[1] / 2,
                    size[0],
                    size[1],
                ),
                width=2,
            )

            return

        # create a drop shadow for the box
        for i in range(1, self.shadow_depth + 1):
            self.draw_rect_alpha(
                self.game.screen,
                (0, 0, 0, self.shadow_intensity),
                (
                    position[0] - size[0] / 2 + i,
                    position[1] - size[1] / 2 + i,
                    size[0],
                    size[1],
                ),
            )

        # draw the blue background
        pygame.draw.rect(
            self.game.screen,
            (0, 0, 255),
            (position[0] - size[0] / 2, position[1] - size[1] / 2, size[0], size[1]),
            width=0,
        )

        # draw the white border
        pygame.draw.rect(
            self.game.screen,
            (255, 255, 255),
            (position[0] - size[0] / 2, position[1] - size[1] / 2, size[0], size[1]),
            width=2,
        )

    def draw_rect_alpha(self, surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)
