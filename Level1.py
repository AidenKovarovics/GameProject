import pygame
import sys
from MoveControl import movement_controls
from WallCheck import touching_wall
from randCoin import rand_coin


def level_one():

    # Initialize pygame
    pygame.init()

    #constants
    screenWidth = 1200
    screenHeight = 792
    mazeStartCoordx = 25
    mazeStartCoordy = 420

    coinCount = 4

    level = 1

    playerCoins = 0

    exitDoor = False

    #screen setup
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    #load background sound
    bgdMusic = pygame.mixer.Sound('level1music.mp3')
    pygame.mixer.Sound.play(bgdMusic)
    bgdMusic.set_volume(0.1)

    #coin collect sound
    coinSound = pygame.mixer.Sound('coincollectsound.mp3')
    coinSound.set_volume(0.2)



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

    #enemy loading
    enemyRect = pygame.Rect(1100, 180, 60, 30)
    enemyMovement = 2

    #enemy image load
    enemyImage = pygame.image.load("enemy rectangle.png").convert_alpha()
    enemyImage = pygame.transform.scale(enemyImage, (enemyRect.width, enemyRect.height))


    enemyRect2 = pygame.Rect(20, 720, 50, 50)
    enemyMovement2 = 2


    enemyImage2 = pygame.image.load("goblin.png").convert_alpha()
    enemyImage2 = pygame.transform.scale(enemyImage2, (enemyRect2.width, enemyRect2.height))

    enemyRect3 = pygame.Rect(420, 300, 50, 50)
    enemyMovement3 = 2

    enemyImage3 = pygame.image.load("squareenemy-removebg-preview.png").convert_alpha()
    enemyImage3 = pygame.transform.scale(enemyImage3, (enemyRect3.width, enemyRect3.height))

    #coin spawning
    coinRects = rand_coin(screen, coinCount, level)

    #door
    doorRect = pygame.Rect(1186, 325, 10, 65)

    #door image load
    doorImage = pygame.image.load("level1Door.png").convert_alpha()
    doorImage = pygame.transform.scale(doorImage, (doorRect.width, doorRect.height))

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
        screen.fill((255, 255, 255))
        screen.blit(grassBackground, (0, 0))
        screen.blit(mazeTemplate, (0, 0))

        screen.blit(playerImage, (playerRect.x, playerRect.y))
        screen.blit(enemyImage, (enemyRect.x, enemyRect.y))
        screen.blit(enemyImage2, (enemyRect2.x, enemyRect2.y))
        screen.blit(enemyImage3, (enemyRect3.x, enemyRect3.y))

        if exitDoor == False:
            screen.blit(doorImage, (doorRect.x, doorRect.y))

        #coin blitting
        for coinRect in coinRects:
            coinImage = pygame.image.load("CoinFrame 1.png").convert_alpha()
            coinImage = pygame.transform.scale(coinImage, (coinRect.width, coinRect.height))
            screen.blit(coinImage, (coinRect.x, coinRect.y))

        storedRect = playerRect.copy()

        #movement controls
        movementLR, movementUD = movement_controls()
        playerRect = playerRect.move(movementLR, movementUD)

        #check for wall collision
        touchingWall = touching_wall(screen, playerRect)
        if touchingWall == True:
            playerRect = storedRect




        #enemy movement
        enemyRect = enemyRect.move(enemyMovement, 0)
        if enemyRect.x >= 1125:
            enemyMovement = -2
        if enemyRect.x <= 960:
            enemyMovement = 2

        enemyRect2 = enemyRect2.move(enemyMovement2, 0)
        if enemyRect2.x >= 420:
            enemyMovement2 = -2
        if enemyRect2.x <= 20:
            enemyMovement2 = 2

        enemyRect3 = enemyRect3.move(0, enemyMovement3)
        if enemyRect3.y >= 480:  # Bottom limit
            enemyMovement3 = -2  # Move up
        if enemyRect3.y <= 250:  # Top limit
            enemyMovement3 = 2  # Move down

        #check for player collision with enemies
        if playerRect.colliderect(enemyRect):
            pygame.mixer.Sound.stop(bgdMusic)
            levelRestart = 'restart'
            return levelRestart

        if playerRect.colliderect(enemyRect2):
            pygame.mixer.Sound.stop(bgdMusic)
            levelRestart = 'restart'
            return levelRestart

        if playerRect.colliderect(enemyRect3):
            pygame.mixer.Sound.stop(bgdMusic)
            levelRestart = 'restart'
            return levelRestart

        #check for player collision with door
        if playerRect.colliderect(doorRect) == True and exitDoor == False:
            playerRect = storedRect
        elif playerRect.colliderect(doorRect) == True and exitDoor == True:
            levelComplete1 = True
            pygame.mixer.Sound.stop(bgdMusic)
            return levelComplete1

        #check for coin collection
        for check in coinRects:
            if playerRect.colliderect(check):
                coinRects.remove(check)
                playerCoins += 1
                pygame.mixer.Sound.play(coinSound)
                if playerCoins == coinCount:
                    exitDoor = True
                    break

        #final screen updates + clock adjustments
        pygame.display.flip()
        pygame.time.Clock().tick(60)
