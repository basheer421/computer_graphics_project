from Rect import Rect
from colors import *
import random

class Drop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(1, 3)  # Randomize drop size
        self.speed = random.uniform(1, 3)  # Randomize drop speed

        self.drop = Rect(x, y, 1, 10 * self.size, fillColor=BLUE, borderColor=BLUE)

    def draw(self):
        self.drop.draw()

    def move(self):
        self.y += self.speed
        self.drop.translate(0, self.speed)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.drop.x = x
        self.drop.y = y

