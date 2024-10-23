import pygame
import sys
from MoveControl import movement_controls
from WallCheck import touching_wall


def level_one():

    #initialize pygame
    pygame.init()

    #constants
    screenWidth = 1200
    screenHeight = 792
    mazeStartCoordx = 0
    mazeStartCoordy = 420

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



        storedRect = playerRect.copy()


        movementLR, movementUD = movement_controls()

        playerRect = playerRect.move(movementLR, movementUD)



        touchingWall = touching_wall(screen, playerRect)

        if touchingWall == True:
            playerRect = storedRect


        #final screen updates + clock adjusts
        pygame.display.flip()
        pygame.time.Clock().tick(60)

level_one()