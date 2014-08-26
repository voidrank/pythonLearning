background_image_filename = "background1.jpg"
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = pygame.image.load(background_image_filename).convert()
while True:
	event = pygame.event.wait()
	if event.type == QUIT:
		exit()
	elif event.type == VIDEORESIZE:
		SCREEN_SIZE = event.size
		screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
		pygame.display.set_caption("Window resized to " + str(event.size))
	screen_width, screen_height = SCREEN_SIZE
	for x in range(0, screen_width, background.get_width()):
		for y in range(0, screen_height, background.get_height()):
			screen.blit(background, (x, y))
	pygame.display.update()