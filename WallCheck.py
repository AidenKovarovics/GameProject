import pygame


def touching_wall(screen, rect):
    # Check all edges: top, bottom, left, and right
    #had to do this because rect.top just gives a center point
    for x in range(rect.left, rect.right):
        if screen.get_at((x, rect.top)) == (0, 0, 0, 255):  # Top edge
            return True
        if screen.get_at((x, rect.bottom - 1)) == (0, 0, 0, 255):  # Bottom edge
            return True
    for y in range(rect.top, rect.bottom):
        if screen.get_at((rect.left, y)) == (0, 0, 0, 255):  # Left edge
            return True
        if screen.get_at((rect.right - 1, y)) == (0, 0, 0, 255):  # Right edge
            return True
    return False