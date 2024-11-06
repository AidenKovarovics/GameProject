import pygame
import random

# List of preset coin spawn locations (tuples of (x, y) coordinates)
coinLocations = [
    (50, 50), (100, 150), (200, 200), (300, 250), (400, 100),
    (150, 300), (250, 400), (350, 50), (450, 150), (500, 300)
]

# List to hold all coin objects (if needed later for updates or interaction)
coinList = []

def rand_coin(screen, count):
    for i in range(count):
        # Select a random spawn location from the coinLocations list
        randX, randY = random.choice(coinLocations)

        # Create a Rect object for the coin's position
        coinRect = pygame.Rect(randX, randY, 50, 50)

        # Optionally, add the coin to the coinList if you want to track it for updates or collision checks
        coinList.append(coinRect)

    return coinList

