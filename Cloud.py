from Circle import Circle

class Cloud:
  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.borderColor = (255, 255, 255)
    self.fillColor = (255, 255, 255)
    # self.circle = Circle(x, y, radius, self.borderColor, self.fillColor)
    """
       pygame.draw.circle(screen, WHITE, (100, 150), 30)
        pygame.draw.circle(screen, WHITE, (120, 150), 30)
        pygame.draw.circle(screen, WHITE, (130, 130), 30)
        pygame.draw.circle(screen, WHITE, (140, 150), 30)
        pygame.draw.circle(screen, WHITE, (160, 150), 30)
    """
    self.circles = [
      Circle(x + (20 * i), y - (20 * (i % 2 != 0)), radius, self.borderColor, self.fillColor)
      for i in range(5)
    ]

  def draw(self):
    for circle in self.circles:
      circle.draw()  

  def translate(self, dx, dy):
    for circle in self.circles:
      circle.translate(dx, dy)
  
  def scale(self, factor):
    for circle in self.circles:
      circle.scale(factor)
