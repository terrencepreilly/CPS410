# This module initializes pygame and runs the main loop for the
# game.
#

import pygame
import sys
from scenes import Menu, Game
from pygame.locals import QUIT

def main():
    pygame.init()
    resolution = (800, 600)
    windowSurface = pygame.display.set_mode(resolution, 0, 32)
    pygame.display.set_caption('Lazer Blast!')
    menu = Menu()
    game = Game()
    active_scene = menu
    
    while True:
        commands = []
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            result = active_scene.update()
            if result == False:
              if active_scene == game:
                active_scene = menu
              elif active_scene == menu:
                active_scene = game

main()
