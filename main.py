import pygame
import sys
from Level1 import level_one


while True:
    level_one()
    restartLevel1 = level_one()
    if restartLevel1 == True:
        level_one()
