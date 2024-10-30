#Jace
import pygame
import sys

pygame.init()
game_sound = pygame.mixer.Sound('cinematic-intro-6097.mp3')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Colors of the Screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Green = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

font_title = pygame.font.Font(None, 74)
font_instructions = pygame.font.Font(None, 36)

title_text = font_title.render("MAZE GAME", True, Green)
instructions_text = font_instructions.render("Press any key to start", True, WHITE)


def start_screen():
    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(instructions_text,
                    (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                running = False

        pygame.display.flip()


def main():
    start_screen()
    #Main Game Loop

if __name__ == "__main__":
    main()
    pygame.quit()