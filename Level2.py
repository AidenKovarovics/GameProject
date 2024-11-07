#Aiden

#have to move with rectanlge to avoid lava
#make platform that swings open and drops blob into lava

import pygame
import sys
from MoveControl import movement_controls
from WallCheck import touching_wall
from randCoin import rand_coin


def level_two():

    #initialize pygame
    pygame.init()

    #constants
    screenWidth = 1200
    screenHeight = 792
    mazeStartCoordx = 25
    mazeStartCoordy = 420

    coinCount = 4

    level = 2

    playerCoins = 0

    exitDoor = False

    #screen setup
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    #load maze template / adjust to scale
    mazeTemplate = pygame.image.load("maze-template-game.svg").convert_alpha()
    mazeTemplate = pygame.transform.rotate(mazeTemplate, 90)
    mazeTemplate = pygame.transform.scale(mazeTemplate, (screenWidth, screenHeight))

    #load grass background
    grassBackground = pygame.image.load("grass-background.PNG").convert()
    grassBackground = pygame.transform.scale(grassBackground, (screenWidth, screenHeight))



    #player
    playerRect = pygame.Rect(mazeStartCoordx, mazeStartCoordy, 44, 30)

    #player image load
    playerImage = pygame.image.load("RemasteredBlob.png").convert_alpha()
    playerImage = pygame.transform.scale(playerImage, (playerRect.width, playerRect.height))

    #enemy
    enemyRect = pygame.Rect(1100, 180, 60, 30)
    enemyMovement = 3

    #enemy image load
    enemyImage = pygame.image.load("enemy rectangle.png").convert_alpha()
    enemyImage = pygame.transform.scale(enemyImage, (enemyRect.width, enemyRect.height))

    #coin spawning
    coinRects = rand_coin(screen, coinCount, level)

    # door
    doorRect = pygame.Rect(1186, 325, 10, 65)

    # door image load
    doorImage = pygame.image.load("level1Door.png").convert_alpha()
    doorImage = pygame.transform.scale(doorImage, (doorRect.width, doorRect.height))

    #main loop
    while True:

        #exit functions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #screen updates
        screen.fill((255,255,255))
        screen.blit(grassBackground, (0,0))
        screen.blit(mazeTemplate, (0, 0))



        screen.blit(playerImage, (playerRect.x, playerRect.y))
        screen.blit(enemyImage,(enemyRect.x, enemyRect.y))

        if exitDoor == False:
            screen.blit(doorImage, (doorRect.x, doorRect.y))


        #coin blitting
        for coinRect in coinRects:
            # Load the coin image and scale it to fit the coinRect
            coinImage = pygame.image.load("CoinFrame 1.png").convert_alpha()
            coinImage = pygame.transform.scale(coinImage, (coinRect.width, coinRect.height))
            screen.blit(coinImage, (coinRect.x, coinRect.y))

        storedRect = playerRect.copy()


        movementLR, movementUD = movement_controls()

        playerRect = playerRect.move(movementLR, movementUD)



        touchingWall = touching_wall(screen, playerRect)

        if touchingWall == True:
            playerRect = storedRect

        #enemy rect movement
        enemyRect = enemyRect.move(enemyMovement, 0)

        if enemyRect.x >= 1125:
            enemyMovement = -1
        if enemyRect.x <= 960:
            enemyMovement = 1

        #check for player collision
        if playerRect.colliderect(enemyRect) == True:
            levelRestart = True
            return levelRestart


        if playerRect.colliderect(doorRect) == True and exitDoor == False:
            playerRect = storedRect
        elif playerRect.colliderect(doorRect) == True and exitDoor == True:
            levelComplete = True
            return levelComplete


        for check in coinRects:
            if playerRect.collideobjects(coinRects) == check:
                coinRects.remove(check)
                playerCoins = playerCoins + 1
                if playerCoins == coinCount:
                    exitDoor = True
                    break





        #final screen updates + clock adjusts
        pygame.display.flip()
        pygame.time.Clock().tick(60)

