import pygame
import random


def rand_coin(screen, count, level):
    if level == 1:
        # level 1 coords
        coinLocations = [
            (50, 50), (100, 150), (200, 200), (300, 250), (400, 100),
            (150, 300), (250, 400), (350, 50), (450, 150), (500, 300)
        ]
    # if level == 2:
    #     level 2 coords

    # List to hold all coin objects (if needed later for updates or interaction)
    coinList = []

    # Generate coins
    for i in range(count):
        # Check for a valid position (not overlapping with other coins)
        valid_position_found = False

        while not valid_position_found:
            # Select a random spawn location from the coinLocations list
            randX, randY = random.choice(coinLocations)

            # Create a Rect object for the coin's position
            coinRect = pygame.Rect(randX, randY, 50, 50)

            # Check if this coin overlaps with any existing coins
            overlap = False
            for existing_coin in coinList:
                if coinRect.colliderect(existing_coin):
                    overlap = True
                    break

            # If no overlap, the position is valid
            if not overlap:
                coinList.append(coinRect)
                valid_position_found = True

    return coinList
