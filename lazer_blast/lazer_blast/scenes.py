import pygame

# This module contains scenes that can be updates interchangeably
# within the main loop of the game.
import pygame
import settings


class Game(object):
    """ The scene containing gameplay. """

    def __init__(self):
        enemies = []
        beams = []
        player = None
        background = None

    def update(self):
        """ Updates the scene and returns true if game is finished
            its execution. """
        return False


class MenuActions:
    """Actions.  Should match the order of items in settings.ITEMS."""
    GAME = 0
    HIGH_SCORES = 1
    EXIT = 2


class _MenuItems(object):

    def __init__(self):
        # Represents the current item selected (which should match
        # MenuActions.)
        self.current = 0
        self.font = pygame.font.SysFont(
            settings.FONT,
            settings.FONT_SIZE,
            )

    def next(self):
        self.current += 1
        if self.current == len(settings.ITEMS):
            self.current = 0

    def prev(self):
        self.current -= 1
        if self.current < 0:
            self.current = len(settings.ITEMS) - 1

    def render(self):
        ret = list()
        for index, item in enumerate(settings.ITEMS):
            curr = ''
            if index == self.current:
                curr = '>    {}'.format(item)
            else:
                curr = '     {}'.format(item)

            label = self.font.render(curr, 1, settings.FONT_COLOR)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (settings.SCREEN_WIDTH / 2) - (width / 2)
            totalHeight = len(settings.ITEMS) * height
            posy = (settings.SCREEN_HEIGHT / 2) - (totalHeight / 2) + (index * height)

            ret.append([label, (posx, posy)])
        return ret


#The menu class implements the main menu for the game, which can
#in turn navigate to the game, a future high score table once the
#scoring system is in place within the game, as well as quitting
#the application.

class Menu(object):
    """The scene containing the title screen and options."""

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.menu_items = _MenuItems()
        self.running = True

    def item_select(self, key):
        if key == pygame.K_UP:
            self.menu_items.prev()
        elif key == pygame.K_DOWN:
            self.menu_items.next()
        elif key == pygame.K_SPACE:
            if self.menu_items.current == MenuActions.GAME:
                pass
            elif self.menu_items.current == MenuActions.HIGH_SCORES:
                pass
            if self.menu_items.current == MenuActions.EXIT:
                self.running = False

    def run(self):
        """Run the menu.

        If the game is exited, the menu will continue running.
        If the menu is exited, then the game ends.
        """
        while self.running:
            # Limit frame speed to 60 FPS
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.item_select(event.key)

            # Redraw the background
            self.screen.fill(settings.BG_COLOR)

            for label, position in self.menu_items.render():
                self.screen.blit(label, position)

            pygame.display.flip()
