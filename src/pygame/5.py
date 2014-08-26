import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = [640, 480]
FULL_SCREEN_SIZE = [1366, 768]
background_image_filename = "background1.jpg"
pygame.init()
screen = pygame.display.set_mode(FULL_SCREEN_SIZE, FULLSCREEN, 32)
Fullscreen = 1
background = pygame.image.load(background_image_filename).convert()

x, y, move_x, move_y = 0, 0, 0, 0

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_F1:
				exit()
			elif event.key == K_F2:
				if Fullscreen:
					screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
				else:
					screen = pygame.display.set_mode(FULL_SCREEN_SIZE, FULLSCREEN, 32)
				Fullscreen = not Fullscreen
			elif event.key == K_LEFT:
				move_x = 1
			elif event.key == K_RIGHT:
				move_x = -1
			elif event.key == K_UP:
				move_y = 1
			elif event.key == K_DOWN:
				move_y = -1
		elif event.type == KEYUP:
			if event.key == K_LEFT:
				if move_x == 1:
					move_x = 0
			elif event.key == K_RIGHT:
				if move_x == -1:
					move_x = 0
			elif event.key == K_UP:
				if move_y == 1:
					move_y = 0
			elif event.key == K_DOWN:
				if move_y == -1:
					move_y = 0
	x += move_x
	if x > 0:
		x = 0
	y += move_y
	if y > 0:
		y = 0
	screen.fill((0,0,0))
	screen.blit(background, (x,y))
	pygame.display.update()
