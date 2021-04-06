import pygame
import random
import time
pygame.init()
WIDTH = 800
HEIGHT = 600
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode(WIDTH, HEIGHT)

background = pygame.image.loadI("")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font = pygame.font.Font("comic.ttf", 40)
