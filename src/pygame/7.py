# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
font = pygame.font.SysFont("宋体", 40)
text_surface = font.render(u"宋体", True, (0,0,255))
x = 0
y = (480-text_surface.get_height())/2
background = pygame.image.load("background1.jpg")
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.blit(background, (0,0))
	x -= 1
	if x < -text_surface.get_width():
		x = SCREEN_SIZE[0]
	screen.blit(text_surface, (x,y))
	pygame.display.update()