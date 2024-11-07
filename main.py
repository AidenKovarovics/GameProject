import pygame
import sys
from Level1 import level_one
from Level2 import level_two

#from Level2 import level_two

while True:
    #level_one()
    #restartLevel1 = level_one()
    #levelComplete1 = level_one()
    #if restartLevel1 == True:
        #level_one()
    #if levelComplete1 == True:
        #level_two()
    level_two()
    restartLevel2 = level_two()
    if restartLevel2 == True:
        level_two()

#add code to keep track of level player is on