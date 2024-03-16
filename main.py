import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Rect import Rect
from Circle import Circle
from Triangle import Triangle
from Cloud import Cloud

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

sky = Rect(0, 0, 800, 300, fillColor=(135/255, 206/255, 235/255))
grass = Rect(0, 300, 800, 300, fillColor=(34/255, 139/255, 34/255))
sun = Circle(70, 70, 40, fillColor=(1, 1, 0))

clouds = [
    Cloud(100, 150, 30),
    # Cloud(300, 150, 30),
    # Cloud(390, 150, 25)
]

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

    # Fill top half with blue for the sky
    sky.draw()

    # Fill bottom half with green for the grass
    grass.draw()

    # Draw yellow sun in the sky
    sun.draw()

    # Draw white cloud shapes in the sky
    for cloud in clouds:
        cloud.draw()


    

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(target_fps)
