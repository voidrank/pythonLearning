import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = [640, 480]
pygame.init()
background_image_filename = "background1.jpg"
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("3_clone")

background = pygame.image.load(background_image_filename).convert()

x, y, dx, dy = 0, 0, 0, 0

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				dx = 1
			elif event.key == K_RIGHT:
				dx = -1
			elif event.key == K_UP:
				dy = 1
			elif event.key == K_DOWN:
				dy = -1
		elif event.type == KEYUP:
			if event.key == K_LEFT:
				if dx == 1:
					dx = 0
			elif event.key == K_RIGHT:
				if dx == -1:
					dx = 0
			elif event.key == K_UP:
				if dy == 1:
					dy = 0
			elif event.key == K_DOWN:
				if dy == -1:
					dy = 0
	x += dx
	y += dy
	screen.fill((0,0,0))
	screen.blit(background, (x,y))
	pygame.display.update()

