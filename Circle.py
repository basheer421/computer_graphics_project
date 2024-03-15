from Shape import *

class Circle(Shape):
  def __init__(self, x, y, radius,
    angle = 0,
    borderColor = (1.0, 1.0, 1.0),
    fillColor = (0, 0, 0)):

    super().__init__(x, y)
    self.radius = radius
    self.angle = angle
    self.borderColor = borderColor
    self.fillColor = fillColor
  
  # Bersenham's circle algorithm
  def draw(self):
    x = 0
    y = self.radius
    d = 3 - 2 * self.radius
    self._drawCircle(x, y)

    while y >= x:
      x += 1
      if d > 0:
        y -= 1
        d = d + 4 * (x - y) + 10
      else:
        d = d + 4 * x + 6
      self._drawCircle(x, y)
  
  def _drawCircle(self, x, y):
    glColor3f(*self.fillColor)
    glBegin(GL_POINTS)
    glVertex2f(self.x + x, self.y + y)
    glVertex2f(self.x - x, self.y + y)
    glVertex2f(self.x + x, self.y - y)
    glVertex2f(self.x - x, self.y - y)
    glVertex2f(self.x + y, self.y + x)
    glVertex2f(self.x - y, self.y + x)
    glVertex2f(self.x + y, self.y - x)
    glVertex2f(self.x - y, self.y - x)
    glEnd()
    glColor3f(*self.borderColor)
    glBegin(GL_LINES)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x + x, self.y + y)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x - x, self.y + y)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x + x, self.y - y)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x - x, self.y - y)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x + y, self.y + x)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x - y, self.y + x)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x + y, self.y - x)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x - y, self.y - x)
    glEnd()
  
  def scale(self, factor):
    self.radius *= factor
    super().scale(factor)
