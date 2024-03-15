import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Rect import Rect
from Circle import Circle

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
            fillColor=(0.7, 0.0, 1.0),
            angle=90)

rect2 = Rect(300, 200, 100, 100,
              borderColor=(1.0, 0.5, 0.0),
              fillColor=(0.7, 0.0, 1.0),
              angle=45)

# Create a circle
circle = Circle(500, 300, 50,
                borderColor=(1.0, 0.5, 0.0),
                fillColor=(0.7, 0.0, 1.0))


# Set up clock for controlling frame rate
clock = pygame.time.Clock()
target_fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    rect.rotate(1)
    rect2.rotate(-5)
    rect.draw()
    rect2.draw()
    circle.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(target_fps)
