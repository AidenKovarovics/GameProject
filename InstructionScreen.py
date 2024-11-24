import pygame
import sys

#Initialize Pygame
pygame.init()

#Set up the display
pygame.display.set_caption("The Adventures of Blob")
WIDTH, HEIGHT = 1200, 792
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_sound = pygame.mixer.Sound('startscreenmusic.mp3')
pygame.mixer.Sound.play(game_sound)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
background_image = pygame.image.load('clouds.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

def show_instructions():
    # Use a larger font size for better visibility
    font = pygame.font.Font('Alucrads.ttf', 48)  # Increase font size for readability

    # Render each line of instructions individually (all text in black)
    text1 = font.render("Welcome to The Adventures of Blob!", True, BLACK)
    text2 = font.render("Blob has entered a mysterious maze land and he must figure a way out...", True, BLACK)
    text3 = font.render("Instructions:", True, BLACK)
    text4 = font.render("1. Use the W,A,S,D keys to move the player.", True, BLACK)
    text5 = font.render("2. Avoid any enemies or creatures in your way, or ELSE.", True, BLACK)
    text6 = font.render("3. To open each gate, you must collect all the hidden coins.", True, BLACK)
    text7 = font.render("4. Press Escape to exit the game.", True, BLACK)
    text8 = font.render("Press any key to start.", True, BLACK)

    # Set up the screen and background
    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))

    # Manually position each line of text on the screen
    screen.blit(text1, (50, 50))
    screen.blit(text2, (50, 110))
    screen.blit(text3, (50, 170))
    screen.blit(text4, (50, 230))
    screen.blit(text5, (50, 290))
    screen.blit(text6, (50, 350))
    screen.blit(text7, (50, 410))
    screen.blit(text8, (50, 470))

    pygame.display.flip()

    # Wait for the player to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
                pygame.mixer.Sound.stop(game_sound)
                return waiting
                break


