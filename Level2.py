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

    platMovement1 = 1
    platMovement2 = 1

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

    #lava pit
    lavaRect1 = pygame.Rect(95, 83, 68, 240)
    lavaRect2 = pygame.Rect(872, 710, 245, 68)

    lavaImage1 = pygame.image.load("lava.png").convert_alpha()
    lavaImage1 = pygame.transform.scale(lavaImage1, (lavaRect1.width, lavaRect1.height))

    lavaImage2 = pygame.image.load("lava.png").convert_alpha()
    lavaImage2 = pygame.transform.rotate(lavaImage2,90)
    lavaImage2 = pygame.transform.scale(lavaImage2, (lavaRect2.width, lavaRect2.height))

    #bridges
    bridgeRect1 = pygame.Rect(95, 65, 68, 120)
    bridgeRect2 = pygame.Rect(850, 710, 120, 68)

    bridgeImage1 = pygame.image.load("bridge_bgd-removebg-preview.png").convert_alpha()
    bridgeImage1 = pygame.transform.rotate(bridgeImage1, 90)
    bridgeImage1 = pygame.transform.scale(bridgeImage1, (bridgeRect1.width, bridgeRect1.height))

    bridgeImage2 = pygame.image.load("bridge_bgd-removebg-preview.png").convert_alpha()
    bridgeImage2 = pygame.transform.scale(bridgeImage2, (bridgeRect2.width, bridgeRect2.height))



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


        screen.blit(dartImage, (dartRect1.x, dartRect1.y))
        screen.blit(dartImage2, (dartRect2.x, dartRect2.y))

        screen.blit(lavaImage1, (lavaRect1.x, lavaRect1.y))
        screen.blit(lavaImage2, (lavaRect2.x, lavaRect2.y))


        screen.blit(bridgeImage1, (bridgeRect1.x, bridgeRect1.y))
        screen.blit(bridgeImage2, (bridgeRect2.x, bridgeRect2.y))

        screen.blit(playerImage, (playerRect.x, playerRect.y))

        #bridge movement
        bridgeRect1 = bridgeRect1.move(0, platMovement1)
        bridgeRect2 = bridgeRect2.move(platMovement2, 0)

        if bridgeRect1.top <= 50:
            platMovement1 = 1
        if bridgeRect1.bottom >= 390:
            platMovement1 = -1

        if bridgeRect2.right >= 1185:
            platMovement2 = -1
        if bridgeRect2.left <= 800:
            platMovement2 = 1



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
                levelRestart = 'restart'
                return levelRestart
        for arrows1 in arrowList2:
            if playerRect.colliderect(arrows1):
                levelRestart = 'restart'
                return levelRestart

        #check for lava collision
        # Initialize onBridge as False
        onBridge = False

        rightBuffer = 20

        # Check if the player is within the vertical bounds of bridgeRect1
        # and horizontally aligned with it (since bridgeRect1 moves up and down)
        if bridgeRect1.left <= playerRect.centerx <= bridgeRect1.right + rightBuffer and bridgeRect1.top <= playerRect.centery <= bridgeRect1.bottom:
            onBridge = True

        # Check if the player is within the horizontal bounds of bridgeRect2
        # and vertically aligned with it (since bridgeRect2 moves left and right)
        elif bridgeRect2.left <= playerRect.centerx <= bridgeRect2.right and bridgeRect2.top <= playerRect.centery <= bridgeRect2.bottom:
            onBridge = True

        # Check for lava collision only if the player is not on a bridge
        if (playerRect.colliderect(lavaRect1) or playerRect.colliderect(lavaRect2)) and not onBridge:
            levelRestart = True
            return 'restart'

        # final screen updates + clock adjusts
        pygame.display.flip()
        pygame.time.Clock().tick(60)


