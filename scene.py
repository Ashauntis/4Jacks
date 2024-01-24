import time
import math


class Scene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.start = time.time()

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
