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

word_speed = 0.5
score = 0


def new_word():
    global displayword, yourword, x_cor, y_cor, text, word_speed
    x_cor = random.randint(300, 700)
    y_cor = 200
    word_speed += 0.10
    yourword = ''
    words = open("words.txt").read().split(',')
    displayword = random.choice(words)


new_word()
font_name = pygame.font.match_font('comic.ttf')


def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, true, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


def game_front_screen():
    gameDisplay.blit(background, (0, 0))
    if not game_over:
        draw_text(gameDisplay, "GAME OVER", 90, WIDTH/2, HEIGHT/4)
        draw_text(gameDisplay, "Score:" + str(score), 70, WIDTH/2, HEIGHT/2)
    else:
        draw_text(gameDisplay, "Press any key to begin", 54, WIDTH/2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
