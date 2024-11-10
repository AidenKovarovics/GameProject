import pygame

def end_screen():
    # Initialize pygame
    pygame.init()

    # Constants
    screenWidth = 1200
    screenHeight = 792
    movementLR = 2  # Speed at which the player moves (adjust as needed)

    # Screen setup
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # Fonts and text rendering
    fontExit = pygame.font.Font('Alucrads.ttf', 50)

    endText = fontExit.render("You Did It! You won!", True, (255,255,255))


    # Load background image
    endBgd = pygame.image.load("endscreen.jpg").convert()
    endBgd = pygame.transform.scale(endBgd, (screenWidth, screenHeight))

    # Load sound (if needed, make sure this works with the file format)
    bgdMusic = pygame.mixer.Sound('level1music.mp3')
    pygame.mixer.Sound.play(bgdMusic)

    # Player setup
    playerRect = pygame.Rect(10, 550, 132, 90)  # Initial position of the player
    playerImage = pygame.image.load("RemasteredBlob.png").convert_alpha()
    playerImage = pygame.transform.scale(playerImage, (playerRect.width, playerRect.height))

    # Main game loop
    clock = pygame.time.Clock()
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return



        # Move player towards the center
        if playerRect.x <= 300:
            movementLR = 2
        if playerRect.x >= 300:
            movementLR = 0

        playerRect = playerRect.move(movementLR, 0)

        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Blit the background
        screen.blit(endBgd, (0, 0))

        # Blit the player
        screen.blit(playerImage, playerRect)

        screen.blit(endText, (100, 200))


        # Update the display
        pygame.display.flip()

        # Limit frame rate to 60 FPS
        clock.tick(60)

# Run the end screen
end_screen()
