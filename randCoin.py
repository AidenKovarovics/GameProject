import pygame
import random

coinList = []
def rand_coin(screen, width, height, count):

    coinImage = pygame.image.load("grass-background.PNG").convert_alpha()
    coinImage = pygame.transform.scale(coinImage, (width, height))
    screen.blit(coinImage, (0, 0))

    while True:
        #loop code to rand gen coords and see if its on a black spot

