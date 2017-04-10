import pygame

FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
COLORS = [
    pygame.color.THECOLORS[x]
    for x in ['red', 'green', 'blue']
]

# Menu Settings
BG_COLOR = (0, 0, 0)
FONT = 'Arial'
FONT_SIZE = 30
FONT_COLOR = (255, 255, 255)
ITEMS = ('Start Game', 'High Scores', 'Quit')

# Player Settings
SPEED = 7
PLAYER_HEALTH = 100
PLAYER_STRENGTH = 1

# Enemy Settings
ENEMY_SPEED = 2
ENEMY_HEALTH = 5
SPAWN_RATE = 0.01
TURN_BOUND = 0.01
ENEMY_STRENGTH = 1

# Control Settings
LEFT = pygame.K_a
DOWN = pygame.K_s
RIGHT = pygame.K_d
UP = pygame.K_w
FIRE = pygame.K_SPACE
SWAP_RIGHT = pygame.K_RIGHT
SWAP_LEFT = pygame.K_LEFT
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
