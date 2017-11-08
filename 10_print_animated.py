import pygame

import random
import math

screenWidth = 800
screenHeight = 800

pygame.init()

pygame.display.set_caption("10 Print in Pygame")
screen = pygame.display.set_mode((screenWidth, screenHeight))
running = True

square = 50

white = (255, 255, 255)
black = (0, 0, 0)


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def rotateLinePoints(start, end, degrees):
    startx, starty = start
    endx, endy = end

    middleX = (startx + endx) // 2
    middleY = (starty + endy) // 2
    inRadians = math.radians(degrees)
    newStart = rotate((middleX, middleY), start, inRadians)
    newEnd = rotate((middleX, middleY), end, inRadians)
    
    return newStart, newEnd

counter = 0

lines = []

for x in range(0, screenWidth, square):
    for y in range(0, screenHeight, square):
        if random.random() > 0.5:           
            lines.append([x, y, x + square, y + square])  
        else:
            lines.append([x, y + square, x + square, y])

# magic numbers: 180, 270, 315, 45, 90
magic_gap = 45
current_frame = 1

def drawScreen():
    global counter, current_frame
    counter += 1

    screen.fill(black)
    for line in lines:
        newStart, newEnd = rotateLinePoints(line[:2], line[2:], counter)
        pygame.draw.line(screen, white, newStart, newEnd, 10)
    
    if (counter % magic_gap) == 0:
        # save more images when things line up
        for i in range(10):
            pygame.image.save(screen, "%05d.png" % current_frame)
            current_frame += 1
    
    else:
        pygame.image.save(screen, "%05d.png" % current_frame)
        current_frame += 1
    
    if current_frame == (360 + 80):
        exit()

while running:
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        drawScreen()
    if key[pygame.K_q]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if you try to quit, let's leave this loop
            running = False
    pygame.display.flip()
