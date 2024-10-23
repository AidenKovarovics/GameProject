
import pygame
import sys


def movement_controls(): #playerColor):
    playerBuffer = 0
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





    return movementLR, movementUD, #playerBuffer



