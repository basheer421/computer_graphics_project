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
    leaveRadius = height / 3
    halfLeaveRadius = leaveRadius / 2
    self.leaves = [
      Circle(trunkTopMiddle[0], trunkTopMiddle[1], leaveRadius, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0] - leaveRadius, trunkTopMiddle[1], leaveRadius, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0] + leaveRadius, trunkTopMiddle[1], leaveRadius, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0], trunkTopMiddle[1] - leaveRadius, leaveRadius, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0] - halfLeaveRadius, trunkTopMiddle[1] - halfLeaveRadius, leaveRadius, fillColor=GREEN, borderColor=GREEN),
      Circle(trunkTopMiddle[0] + halfLeaveRadius, trunkTopMiddle[1] - halfLeaveRadius, leaveRadius, fillColor=GREEN, borderColor=GREEN)
    ]
  
  def draw(self):
    self.trunk.draw()
    for leaf in self.leaves:
      leaf.draw()
  
  def scale(self, factor):
    self.__init__(self.x, self.y, self.width * factor, self.height * factor)
  
  def translate(self, dx, dy):
    self.x += dx
    self.y += dy
    self.trunk.translate(dx, dy)
    for leaf in self.leaves:
      leaf.translate(dx, dy)
  
  def animate(self):
    self.scale(1.0008)
    self.translate(0, -0.1)
