import pygame
import sys
from Level1 import level_one
#from Level2 import level_two

while True:
    level_one()
    restartLevel1 = level_one()
    levelComplete1 = level_one()
    if restartLevel1 == True:
        level_one()
    #if levelComplete1 == True:
        #level_two()
