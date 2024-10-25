import pygame
import sys
from Level1 import level_one


while True:
    level_one()
    restartLevel = level_one()
    if restartLevel == True:
        level_one()
