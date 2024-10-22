
import pygame
import sys


def movement(startx, starty):

    #initialize rect at starting coord and movement = 0
    playerRect = pygame.Rect((startx, starty), (10, 10))


    movementUD = 0
    movementLR = 0

    # movement controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        movementLR = -5
    if keys[pygame.K_d]:
        movementLR = 5
    if keys[pygame.K_s]:
        movementUD = 5
    if keys[pygame.K_w]:
        movementUD = -5


    movingPlayer = playerRect.move(movementLR, movementUD)


