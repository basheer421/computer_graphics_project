import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Shape import Shape
from Rect import Rect

# Initialize Pygame
pygame.init()

# Set up display
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Computer graphics scene")

# Set up OpenGL orthographic projection for 2D rendering
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, display[0], display[1], 0, -1, 1)
glMatrixMode(GL_MODELVIEW)

rect = Rect(100, 100, 100, 100,
  borderColor=(1.0, 0.5, 0.0),
  fillColor=(0.7, 0.0, 1.0)
  )
print(rect)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or \
      (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      pygame.quit()
      quit()

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rect.draw()

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)
