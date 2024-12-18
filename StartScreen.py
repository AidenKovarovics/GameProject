

import pygame
import sys



def start_screen():
    pygame.init()

    # Load sound and background image
    game_sound = pygame.mixer.Sound('startscreenmusic.mp3')
    pygame.mixer.Sound.play(game_sound)

    # Screen dimensions and colors
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 792
    WHITE = (255, 255, 255)

    background_image = pygame.image.load('startscreen-overlay.jpg')
    background_image = pygame.transform.scale(background_image,
                                              (SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Start Screen")

    font_title = pygame.font.Font('Alucrads.ttf', 150)
    font_instructions = pygame.font.Font('Alucrads.ttf', 80)

    title_text = font_title.render("The Adventures of Blob", True, WHITE)
    instructions_text = font_instructions.render("Press any key to start", True, WHITE)

    # Scale the background image to fit the screen
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        screen.blit(background_image, (0, 0))  # Draw the background image
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 80))
        screen.blit(instructions_text,
                    (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, 700))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.stop(game_sound)
                running = False
                return running


        pygame.display.flip()



