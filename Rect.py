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

	def draw(self):
		glPushMatrix()

		glTranslatef(self.center[0], self.center[1], 0)
		glRotatef(self.angle, 0, 0, 1)
		glTranslatef(-self.center[0], -self.center[1], 0)

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

		glPopMatrix()
