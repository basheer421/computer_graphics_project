from Rect import Rect
from Circle import Circle
from colors import *

class Tree:
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.trunk = Rect(x, y, width, height, fillColor=BROWN, borderColor=BROWN)
    trunkTopMiddle = (x + width / 2, y)
    self.leaves = [
      Circle(trunkTopMiddle[0], trunkTopMiddle[1], 50, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0] - 50, trunkTopMiddle[1], 50, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0] + 50, trunkTopMiddle[1], 50, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0], trunkTopMiddle[1] - 50, 50, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0] - 25, trunkTopMiddle[1] - 25, 50, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0] + 25, trunkTopMiddle[1] - 25, 50, fillColor=GREEN, borderColor=GREEN)
    ]
  
  def draw(self):
    self.trunk.draw()
    for leaf in self.leaves:
      leaf.draw()
