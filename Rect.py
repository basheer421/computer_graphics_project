from Shape import *

class Rect(Shape):
  def __init__(self, x, y, width, height,
    angle = 0,
    borderColor = (1.0, 1.0, 1.0),
    fillColor = (0, 0, 0)):

    super().__init__(x, y)
    self.width = width
    self.height = height
    self.angle = angle
    self.borderColor = borderColor
    self.fillColor = fillColor

  def draw(self):
    glColor3f(*self.fillColor)
    glRectf(self.x, self.y, self.x + self.width, self.y + self.height)

    glColor3f(*self.borderColor)
    glBegin(GL_LINES)
    glVertex2f(self.x, self.y)
    glVertex2f(self.x + self.width, self.y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(self.x + self.width, self.y)
    glVertex2f(self.x + self.width, self.y + self.height)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(self.x + self.width, self.y + self.height)
    glVertex2f(self.x, self.y + self.height)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(self.x, self.y + self.height)
    glVertex2f(self.x, self.y)
    glEnd()
