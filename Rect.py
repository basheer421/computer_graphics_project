import math

from Shape import *


class Rect(Shape):
    def __init__(self, x, y, width, height,
                 angle=0,
                 borderColor=(1.0, 1.0, 1.0),
                 fillColor=(0, 0, 0)):

        super().__init__(x, y)
        self.width = width
        self.height = height
        self.borderColor = borderColor
        self.fillColor = fillColor

        # Calculate the center of the rectangle
        self.center = (self.x + self.width / 2, self.y + self.height / 2)

        # Initialize vertices
        self.vertices = [
            (self.x, self.y),
            (self.x + self.width, self.y),
            (self.x + self.width, self.y + self.height),
            (self.x, self.y + self.height)
        ]

        # Rotate the rectangle
        self.rotate(angle)

    def rotate(self, angle):
        super().rotate(angle)
        _angle = math.radians(self.angle)
        _cos = math.cos(_angle)
        _sin = math.sin(_angle)

        def _rotatePoint(x, y, center_x, center_y, cos, sin):
            # Translate point to the origin (center of the rectangle)
            x -= center_x
            y -= center_y
            # Rotate around the origin
            new_x = x * cos - y * sin
            new_y = x * sin + y * cos
            # Translate back to the original position
            return new_x + center_x, new_y + center_y

        # Rotate each vertex around the center of the rectangle
        self.vertices = [
            _rotatePoint(x, y, *self.center, _cos, _sin)
            for x, y in self.vertices
        ]

    def draw(self):

        glColor3f(*self.fillColor)
        glBegin(GL_QUADS)
        for x, y in self.vertices:
            glVertex2f(x, y)
        glEnd()

        glColor3f(*self.borderColor)
        glBegin(GL_LINES)
        for i in range(4):
            glVertex2f(*self.vertices[i])
            glVertex2f(*self.vertices[(i + 1) % 4])
        glEnd()
