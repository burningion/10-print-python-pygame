import pygame

import random

screenHeight, screenWidth = (800, 800)

pygame.init()

pygame.display.set_caption("10 Print in Pygame")
screen = pygame.display.set_mode((screenWidth, screenHeight))

running = True

white = (255, 255, 255)
black = (0, 0, 0)

square = 20

def drawScreen():
    screen.fill(black)
    for x in range(0, screenWidth, square):
        for y in range(0, screenHeight, square):
            if random.random() > 0.5:
                pygame.draw.line(screen, white, (x, y), (x + square, y + square))
            else:
                pygame.draw.line(screen, white, (x, y + square), (x + square, y))

while running:
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        drawScreen()
    if key[pygame.K_q]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()