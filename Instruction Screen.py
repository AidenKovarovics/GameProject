#Jace
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
background_image = pygame.image.load

def show_instructions():
    font = pygame.font.Font('Alucrads.ttf', 36)  # Use a smaller font size for better fit
    instructions = [
        "Welcome to The Adventures of Blob!",
        "Blob has entered a mysterious maze land and he must figure a way out...",
        "Instructions:",
        "1. Use the W,A,S,D keys to move the player.",
        "2. Avoid any enemies or creatures your way or ELSE.",
        "3. To Open each gate, you must collect all the hidden coins.",
        "4. Good Luck, my friends...",
        
        "Press any key to start."
    ]

    screen.fill(BLACK)
    for i, line in enumerate(instructions):
        text = font.render(line, True, WHITE)
        screen.blit(text, (50, 50 + i * 40))
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

# Call the instructions function
show_instructions()