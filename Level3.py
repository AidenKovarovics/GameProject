import pygame



def end_screen():
    # Initialize pygame
    pygame.init()

    #constants
    screenWidth = 1200
    screenHeight = 792
    movementLR = 2

    #screen setup
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    #fonts and text
    fontExit = pygame.font.Font('Alucrads.ttf', 50)

    endText = fontExit.render("You Did It! You won!", True, (255,255,255))


    #load background image
    endBgd = pygame.image.load("endscreen.jpg").convert()
    endBgd = pygame.transform.scale(endBgd, (screenWidth, screenHeight))

    #load sound
    bgdMusic = pygame.mixer.Sound('freaxy-de-small-thamba-lam-252976.mp3')
    pygame.mixer.Sound.play(bgdMusic)

    #moving blob image load
    playerRect = pygame.Rect(10, 550, 132, 90)
    playerImage = pygame.image.load("RemasteredBlob.png").convert_alpha()
    playerImage = pygame.transform.scale(playerImage, (playerRect.width, playerRect.height))

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #blob movement
        if playerRect.x <= 300:
            movementLR = 2
        if playerRect.x >= 300:
            movementLR = 0
            pygame.quit()

        playerRect = playerRect.move(movementLR, 0)

        #fill the screen
        screen.fill((255, 255, 255))


        screen.blit(endBgd, (0, 0))

        screen.blit(playerImage, playerRect)

        screen.blit(endText, (100, 200))


        pygame.display.flip()

        clock.tick(60)

