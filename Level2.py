import pygame
import sys
from MoveControl import movement_controls
from WallCheck import touching_wall
from randCoin import rand_coin
import time


def level_two():
    # initialize pygame
    pygame.init()

    # constants
    screenWidth = 1200
    screenHeight = 792
    mazeStartCoordx = 25
    mazeStartCoordy = 30

    coinCount = 4
    level = 2
    playerCoins = 0
    exitDoor = False

    # screen setup
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # load maze template / adjust to scale
    mazeTemplate = pygame.image.load("level2Maze.svg").convert_alpha()
    mazeTemplate = pygame.transform.rotate(mazeTemplate, 90)
    mazeTemplate = pygame.transform.scale(mazeTemplate, (screenWidth, screenHeight))

    # load grass background
    grassBackground = pygame.image.load("level2Floor.png").convert()
    grassBackground = pygame.transform.scale(grassBackground, (screenWidth, screenHeight))

    # player
    playerRect = pygame.Rect(mazeStartCoordx, mazeStartCoordy, 44, 30)

    # player image load
    playerImage = pygame.image.load("RemasteredBlob.png").convert_alpha()
    playerImage = pygame.transform.scale(playerImage, (playerRect.width, playerRect.height))

    # enemy dart boards
    dartRect1 = pygame.Rect(566, 330, 15, 127)
    dartRect2 = pygame.Rect(890, 531, 127, 15)

    # Define each arrow Rect directly with hardcoded positions (right arrows)
    arrowRect1 = pygame.Rect(575, 335, 25, 8)
    arrowRect2 = pygame.Rect(575, 390, 25, 8)  # 15 pixels lower than arrowRect1
    arrowRect3 = pygame.Rect(575, 445, 25, 8)  # 15 pixels lower than arrowRect2

    # Define each arrow Rect for downward movement (from second dart shooter)
    arrowRect4 = pygame.Rect(890, 530, 8, 25)  # Adjust for downward arrows
    arrowRect5 = pygame.Rect(945, 530, 8, 25)  # 15 pixels lower than arrowRect4
    arrowRect6 = pygame.Rect(1000, 530, 8, 25)  # 15 pixels lower than arrowRect5

    # Load arrow images
    arrowImage = pygame.image.load("enemyarrow.png").convert_alpha()
    arrowImage = pygame.transform.scale(arrowImage, (25, 8))

    # Rotate arrow 2 for downward movement
    arrowImage2 = pygame.image.load("enemyarrow.png").convert_alpha()
    arrowImage2 = pygame.transform.rotate(arrowImage2, 90)  # Rotate for downward movement
    arrowImage2 = pygame.transform.scale(arrowImage2, (8, 25))

    # enemy dart board 1 image load
    dartImage = pygame.image.load("dartshooter.png").convert_alpha()
    dartImage = pygame.transform.scale(dartImage, (dartRect1.width, dartRect1.height))

    # enemy dart board 2
    dartImage2 = pygame.image.load("dartshooter.png").convert_alpha()
    dartImage2 = pygame.transform.rotate(dartImage2, 90)
    dartImage2 = pygame.transform.scale(dartImage2, (dartRect2.width, dartRect2.height))

    # coin spawning
    coinRects = rand_coin(screen, coinCount, level)

    # door
    doorRect = pygame.Rect(1186, 325, 10, 65)

    # door image load
    doorImage = pygame.image.load("level1Door.png").convert_alpha()
    doorImage = pygame.transform.scale(doorImage, (doorRect.width, doorRect.height))

    # main loop
    while True:
        # exit functions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # screen updates
        screen.fill((255, 255, 255))
        screen.blit(grassBackground, (0, 0))
        screen.blit(mazeTemplate, (0, 0))

        screen.blit(playerImage, (playerRect.x, playerRect.y))
        screen.blit(dartImage, (dartRect1.x, dartRect1.y))
        screen.blit(dartImage2, (dartRect2.x, dartRect2.y))

        # Arrow movement and blitting (right arrows)
        arrowList1 = [arrowRect1, arrowRect2, arrowRect3]
        arrowList2 = [arrowRect4, arrowRect5, arrowRect6]
        for arrowRect in arrowList1:
            # Move arrow right
            arrowRect.x += 1  # Move by 1 pixel to the right

            # Reset arrow position if it reaches the end point
            if arrowRect.x >= 770:
                arrowRect.x = 575  # Reset to initial x position

            # Blit each arrow
            screen.blit(arrowImage, (arrowRect.x, arrowRect.y))

        # Arrow movement and blitting (downward arrows)
        for arrowRect in arrowList2:
            # Move arrow downward
            arrowRect.y -= 1  # Move by 1 pixel downward

            # Reset arrow position if it reaches the bottom
            if arrowRect.y <= 245:
                arrowRect.y = 530  # Reset to initial y position (adjust this if needed)

            # Blit each downward arrow
            screen.blit(arrowImage2, (arrowRect.x, arrowRect.y))

        if not exitDoor:
            screen.blit(doorImage, (doorRect.x, doorRect.y))

        # coin blitting
        for coinRect in coinRects:
            # Load the coin image and scale it to fit the coinRect
            coinImage = pygame.image.load("CoinFrame 1.png").convert_alpha()
            coinImage = pygame.transform.scale(coinImage, (coinRect.width, coinRect.height))
            screen.blit(coinImage, (coinRect.x, coinRect.y))

        storedRect = playerRect.copy()

        movementLR, movementUD = movement_controls()
        playerRect = playerRect.move(movementLR, movementUD)

        touchingWall = touching_wall(screen, playerRect)

        if touchingWall:
            playerRect = storedRect

        # check for player collision with door
        if playerRect.colliderect(doorRect) and not exitDoor:
            playerRect = storedRect
        elif playerRect.colliderect(doorRect) and exitDoor:
            levelComplete = True
            return levelComplete

        # check for player collision with coins
        for check in coinRects:
            if playerRect.colliderect(check):
                coinRects.remove(check)
                playerCoins += 1
                if playerCoins == coinCount:
                    exitDoor = True
                    break

        #check for dart board collision
        dartboards = [dartRect1, dartRect2]
        if playerRect.collideobjects(dartboards) == dartRect1 or playerRect.collideobjects(dartboards) == dartRect2:
            playerRect = storedRect

        #check for arrow collision
        for arrows in arrowList1:
            if playerRect.colliderect(arrows):
                levelRestart = True
                return levelRestart
        for arrows1 in arrowList2:
            if playerRect.colliderect(arrows1):
                levelRestart = True
                return levelRestart


        # final screen updates + clock adjusts
        pygame.display.flip()
        pygame.time.Clock().tick(60)


