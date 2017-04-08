# This module initializes pygame and runs the main loop for the
# game.

import pygame
from lazer_blast import settings
from lazer_blast.scenes import Menu


def main():
    pygame.init()
    windowSurface = pygame.display.set_mode(
        settings.SCREEN_DIMENSIONS, 0, 32
    )
    pygame.display.set_caption('Lazer Blast!')
    menu = Menu(windowSurface)
    menu.run()


if __name__ == '__main__':
    main()
