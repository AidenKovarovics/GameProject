import pygame
import sys
from Level1 import level_one
from Level2 import level_two


# Track the current level
current_level = 1

while True:
    if current_level == 1:
        result = level_one()  # Run level one and store result
        if result == True:  # If level_one returns levelComplete (level is complete)
            current_level = 2  # Move to level two
        elif result == "restart":  # If level_one returns levelRestart (level needs to restart)
            continue  # Restart level one

    elif current_level == 2:
        result = level_two()  # Run level two and store result
        if result == "restart":  # If level_two returns levelRestart
            continue  # Restart level two

