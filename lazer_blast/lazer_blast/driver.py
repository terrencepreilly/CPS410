# This module initializes pygame and runs the main loop for the
# game.
#

import pygame
import sys
from scenes import Menu, MenuActions
from pygame.locals import QUIT
import settings


if __name__ == '__main__':
    pygame.init()
    windowSurface = pygame.display.set_mode(
        settings.SCREEN_DIMENSIONS, 0, 32
        )
    pygame.display.set_caption('Lazer Blast!')
    menu = Menu(windowSurface)
    menu.run()
