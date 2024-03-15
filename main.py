import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
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
            fillColor=(0.7, 0.0, 1.0),
            angle=90)

# Set up clock for controlling frame rate
clock = pygame.time.Clock()
target_fps = 60

# Initial angle and angular velocity
angle = 0
angular_velocity = 0.1  # Degrees per second

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Calculate the elapsed time since the last frame
    dt = clock.tick(target_fps) / 1000.0  # Convert milliseconds to seconds

    # Update the angle based on angular velocity and elapsed time
    angle += angular_velocity * dt

    # Draw and rotate the rectangle
    rect.rotate(angle)
    rect.draw()

    # Update the display
    pygame.display.flip()
