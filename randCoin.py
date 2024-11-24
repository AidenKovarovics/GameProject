import pygame
import random


def rand_coin(screen, count, level):


    if level == 1:
        # level 1 coords
        coinLocations = [
            (355, 283), (363, 352), (269, 664), (186, 589), (998, 120), (1044, 283), (975, 512), (983, 585)#figure out good coords for coins
        ]
    if level == 2:
        #level 2 coords
        coinLocations = [
            (28, 729), (112, 495), (176, 27), (574, 105), (419, 479), (907,271), (1052, 181), (974,567), (719, 352), (1129, 262)
            ]


    #list to hold all coins
    coinList = []

    for i in range(count):
        validPos = False

        while not validPos:
            randX, randY = random.choice(coinLocations)

            coinRect = pygame.Rect(randX, randY, 32, 32)

            overlap = False
            for existing_coin in coinList:
                if coinRect.colliderect(existing_coin):
                    overlap = True
                    break

            if not overlap:
                coinList.append(coinRect)
                validPos = True

    return coinList
