from Shape import *

class Circle(Shape):
	def __init__(self, x, y, radius,
		borderColor = (1.0, 1.0, 1.0),
		fillColor = (0, 0, 0)):

		super().__init__(x, y)
		self.radius = radius
		self.borderColor = borderColor
		self.fillColor = fillColor
		self._genVertices()

	def _genVertices(self):
		self.vertices = []
		x = 0
		y = self.radius
		d = 3 - 2 * self.radius
		self.vertices.append((x, y))

		while y >= x:
			x += 1
			if d > 0:
				y -= 1
				d = d + 4 * (x - y) + 10
			else:
				d = d + 4 * x + 6
			self.vertices.append((x, y))

	
	# Bersenham's circle algorithm
	def draw(self):
		glPushMatrix()
		glTranslatef(self.x, self.y, 0)
		glBegin(GL_POINTS)
		for x, y in self.vertices:
			self._drawCircle(x, y)
		glEnd()
		glPopMatrix()
	
	def _drawCircle(self, x, y):
		glColor3f(*self.borderColor)
		glVertex2f(x, y)
		glVertex2f(-x, y)
		glVertex2f(x, -y)
		glVertex2f(-x, -y)
		glVertex2f(y, x)
		glVertex2f(-y, x)
		glVertex2f(y, -x)
		glVertex2f(-y, -x)

	def scale(self, factor):
		self.radius *= factor
		super().scale(factor)
