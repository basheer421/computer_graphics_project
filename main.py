import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from colors import *
from Rect import Rect
from Circle import Circle
from Triangle import Triangle
from Cloud import Cloud
from Tree import Tree

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

sky = Rect(0, 0, 800, 300, fillColor=BLUE, borderColor=BLUE)
grass = Rect(0, 300, 800, 300, fillColor=DGREEN, borderColor=DGREEN)
sun = Circle(70, 70, 40, fillColor=YELLOW, borderColor=YELLOW)

clouds = [
    Cloud(100, 150, 30),
    Cloud(300, 180, 30),
    Cloud(390, 120, 25),
    Cloud(500, 160, 30),
    Cloud(600, 155, 30)
]

trees = [
    Tree(120, 400, 20, 100)
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
    
    # Draw green tree shapes on the grass
    for tree in trees:
        tree.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(target_fps)
