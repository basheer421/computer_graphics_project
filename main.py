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
from Person import Person
from Drop import Drop
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
display = (SCREEN_WIDTH, SCREEN_HEIGHT)
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

# Initialize raindrops
rain = []
for cloud in clouds:
		for i in range(10):
				drop = Drop(cloud.x + random.randint(-20, 20), cloud.y + random.randint(-20, 20))
				rain.append(drop)

# Animate raindrops
def animate_rain():
		for drop in rain:
				drop.move()
				if drop.y > SCREEN_HEIGHT:  # If drop falls off the screen, reset it
						drop.reset(drop.x, random.randint(-20, -10))
				drop.draw()

tree = Tree(120, 400, 10, 50)

person = Person((250, 450))

water_lake = Circle(display[0], person.hands[0].y, 90, fillColor=BLUE, borderColor=BLUE)

scenes = [True, False, False]
# Set up clock for controlling frame rate
clock = pygame.time.Clock()
target_fps = 60
ADDAPPLES = pygame.USEREVENT + 1
SCENE1END = pygame.USEREVENT + 2
SCENE2START = pygame.USEREVENT + 3
SCENE2END = pygame.USEREVENT + 4

pygame.time.set_timer(ADDAPPLES, 15000, loops=1) # 15 seconds
pygame.time.set_timer(SCENE1END, 20000, loops=1) # 20 seconds
pygame.time.set_timer(SCENE2START, 21000, loops=1) # 20 seconds
pygame.time.set_timer(SCENE2END, 30000, loops=1) # 30 seconds

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or \
				(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			quit()
		if (event.type == ADDAPPLES):
			tree.addApples()
		elif (event.type == SCENE1END):
			scenes[0] = False
		elif (event.type == SCENE2START):
			scenes[1] = True
		elif (event.type == SCENE2END):
			scenes[1] = False

	# Clear the screen and depth buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	time = pygame.time.get_ticks() // 1000

	
	if (scenes[0] == True):
		# Scenery
		sky.draw()
		grass.draw()
		sun.draw()
		person.draw()
		water_lake.draw()
		if (time > 5):
			tree.draw()

		for cloud in clouds:
			cloud.animate()
			cloud.draw()
		
		animate_rain()

		if (time > 5) and (time < 19):
			tree.animate()
			# water = Rect(person.hands[0].x, person.hands[0].y, 50, 10, 20,
			# 	fillColor=BLUE, borderColor=BLUE)
			# water_start = Circle(person.hands[0].x, person.hands[0].y + 5, 8,
			# 	fillColor=BLUE, borderColor=BLUE)
			# water.translate(-50, -10)
			# water.draw()
			# water_start.draw()
		
		if (time < 4):
			person.translate(-person.dx, 0)
			# water_pipe.translate(-person.dx, 0)
	elif (scenes[1] == True):
		sky.draw()
		grass.draw()
		sun.draw()
		person.draw()
		water_lake.draw()
		tree.draw()
		for cloud in clouds:
			cloud.draw()
		if (time < 29):
			person.translate(person.dx, 0)
	pygame.display.flip()
	clock.tick(target_fps)
