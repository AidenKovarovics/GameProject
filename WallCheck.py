import pygame


def touching_wall(screen, rect):
    #check all edges of rect
    for x in range(rect.left, rect.right):
        if screen.get_at((x, rect.top)) == (0, 0, 0, 255):
            return True
        if screen.get_at((x, rect.bottom - 1)) == (0, 0, 0, 255):
            return True
    for y in range(rect.top, rect.bottom):
        if screen.get_at((rect.left, y)) == (0, 0, 0, 255):
            return True
        if screen.get_at((rect.right - 1, y)) == (0, 0, 0, 255):
            return True
    return False