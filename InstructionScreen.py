import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
pygame.display.set_caption("The Adventures of Blob")
WIDTH, HEIGHT = 1200, 792
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
    text7 = font.render("4. Good Luck, my friends...", True, BLACK)
    text8 = font.render("Press any key to start.", True, BLACK)

    # Set up the screen and background
    screen.fill(WHITE)  # Fill screen with white, as text is black now
    screen.blit(background_image, (0, 0))

    # Manually position each line of text on the screen
    screen.blit(text1, (50, 50))  # First line of text
    screen.blit(text2, (50, 110))  # Second line of text
    screen.blit(text3, (50, 170))  # Third line of text
    screen.blit(text4, (50, 230))  # Fourth line of text
    screen.blit(text5, (50, 290))  # Fifth line of text
    screen.blit(text6, (50, 350))  # Sixth line of text
    screen.blit(text7, (50, 410))  # Seventh line of text
    screen.blit(text8, (50, 470))  # Eighth line of text

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
                return waiting
                break


