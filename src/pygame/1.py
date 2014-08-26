#! -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit

background_image_filename = "background_comp.jpg"
pygame.init()
#init
screen = pygame.display.set_mode((1067,600), 0, 32)
#set screen

pygame.display.set_caption("mono gatari")
background = pygame.image.load(background_image_filename).convert()

while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			screen.blit(background, (0,0))
			pygame.display.update()
