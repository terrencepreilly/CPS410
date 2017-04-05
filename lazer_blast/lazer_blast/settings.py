import pygame

FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Menu Settings
BG_COLOR = (0, 0, 0)
FONT = 'Arial'
FONT_SIZE = 30
FONT_COLOR = (255, 255, 255)
ITEMS = ('Start Game', 'High Scores', 'Quit')

# Player Settings
SPEED = 5

# Control Settings
LEFT = pygame.K_a
DOWN = pygame.K_s
RIGHT = pygame.K_d
UP = pygame.K_w
FIRE = pygame.K_SPACE
SWAP_RIGHT = pygame.K_e
SWAP_LEFT = pygame.K_q
ESCAPE = pygame.K_ESCAPE

_dvorak = False
if _dvorak:
    LEFT = pygame.K_a
    DOWN = pygame.K_o
    RIGHT = pygame.K_e
    UP = pygame.K_COMMA
    FIRE = pygame.K_SPACE
    SWAP_RIGHT = pygame.K_PERIOD
    SWAP_LEFT = pygame.K_QUOTE
    ESCAPE = pygame.K_ESCAPE
