# This module contains scenes that can be updates interchangeably
# within the main loop of the game.
import os
import pygame
from random import Random
import yaml

from lazer_blast import settings
from lazer_blast.ships import (
    Enemy,
    Player,
    HealthBar,
    ScoreBoard,
)


class Game(object):
    """ The scene containing gameplay. """

    def __init__(self, screen):
        self.surface = pygame.Surface(settings.SCREEN_DIMENSIONS)
        self.beams = []
        self.enemies = list()
        self.player = Player()
        self.player.surface = self.surface
        self.background = None
        self.running = True
        self.game_over = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.rand = Random()
        self.health_bar = HealthBar(player=self.player)
        self.score_board = ScoreBoard()

    def generate_enemies(self):
        if self.rand.random() < settings.SPAWN_RATE:
            x = self.rand.randint(0, settings.SCREEN_DIMENSIONS[0])
            color = self.rand.choice(settings.COLORS)
            enemy = Enemy(starting_pos=(x, 0), color=color)
            enemy.target = self.player
            enemy.surface = self.surface
            self.enemies.append(
                enemy
            )

    def handle_keydown(self, key):
        if key == settings.LEFT:
            self.player.momentum = (-1, self.player.momentum[1])
        elif key == settings.DOWN:
            self.player.momentum = (self.player.momentum[0], 1)
        elif key == settings.RIGHT:
            self.player.momentum = (1, self.player.momentum[1])
        elif key == settings.UP:
            self.player.momentum = (self.player.momentum[0], -1)
        elif key == settings.FIRE:
            self.player.flip_laser(True)
        elif key == settings.SWAP_RIGHT:
            self.player.next_color()
        elif key == settings.SWAP_LEFT:
            self.player.prev_color()
        elif key == settings.ESCAPE:
            self.running = False

    def handle_keyup(self, key):
        if key == settings.LEFT:
            self.player.momentum = (0, self.player.momentum[1])
        elif key == settings.DOWN:
            self.player.momentum = (self.player.momentum[0], 0)
        elif key == settings.RIGHT:
            self.player.momentum = (0, self.player.momentum[1])
        elif key == settings.UP:
            self.player.momentum = (self.player.momentum[0], 0)
        elif key == settings.FIRE:
            self.player.flip_laser(False)

    def run(self):
        self.running = True
        settings.ITEMS = ('Resume', settings.ITEMS[1], settings.ITEMS[2])
        while self.running:
            # Limit frame speed to 60 FPS
            self.clock.tick(settings.FPS)
            self.handle_key_events()
            self.render_items()
            self.handle_collisions()
            self.score_board.add_points(
                sum([1 for x in self.enemies if x.health <= 0])
            )
            self.enemies = [x for x in self.enemies
                            if x.in_bounds() and x.health > 0]
            self.generate_enemies()

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)
            if event.type == pygame.KEYUP:
                self.handle_keyup(event.key)

    def render_items(self):
        self.screen.fill(settings.BG_COLOR)
        for enemy in self.enemies:
            enemy.render(self.screen)
        self.player.render(self.screen)
        self.health_bar.render(self.screen)
        self.score_board.render(self.screen)

        # Once there are images, this is what should be rendered
        for enemy in self.enemies:
            next(enemy)
        next(self.player)
        next(self.health_bar)
        pygame.display.flip()

    def handle_collisions(self):
        if self.player.enemies_touching(self.enemies):
            self.player.health -= settings.ENEMY_STRENGTH
            if self.player.health <= 0:
                self.player.PlaySound("275008__alienxxx__mayday-mayday.wav")
                pygame.time.wait(2700)
                self.player.PlaySound("35462__jobro__explosion-5.wav")
                self.running = False
                self.game_over = True


class HighScores(object):

    def __init__(self, screen):
        self.path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'assets/high_scores.yaml',
        )
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.scores = None
        self.running = True
        self.load()
        self.font = pygame.font.SysFont(
            settings.FONT,
            settings.FONT_SIZE,
        )

    def load(self):
        with open(self.path, 'r') as fin:
            self.scores = yaml.load(fin)
        if self.scores is None:
            self.scores = list()

    def add_score(self, score):
        self.scores.append(score * 10)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:10]

    def save(self):
        with open(self.path, 'w') as fout:
            yaml.dump(self.scores, fout)

    def render(self):
        label = self.font.render('High Scores', 1, settings.FONT_COLOR)
        curr_y = settings.SCREEN_HEIGHT * 0.25
        x = settings.SCREEN_WIDTH * 0.5 - label.get_rect().width / 2
        self.screen.blit(label, (x, curr_y))
        curr_y += label.get_rect().height + 5
        for score in self.scores:
            label = self.font.render(str(score), 1, settings.FONT_COLOR)
            self.screen.blit(label, (x, curr_y))
            curr_y += label.get_rect().height + 5

    def handle_key_events(self):
        # Any key
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(settings.FPS)
            self.handle_key_events()
            self.screen.fill(settings.BG_COLOR)
            self.render()
            pygame.display.flip()


class MenuActions:
    """Actions.  Should match the order of items in settings.ITEMS."""
    GAME = 0
    HIGH_SCORES = 1
    EXIT = 2


class _MenuItems(object):

    def __init__(self, game):
        # Represents the current item selected (which should match
        # MenuActions.)
        self.current = 0
        self.game = game
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
        items = None
        if not self.game.game_over:
            items = settings.ITEMS
        else:
            items = settings.GAME_OVER_ITEMS

        for index, item in enumerate(items):
            curr = ''
            if index == self.current:
                curr = '>    {}'.format(item)
            else:
                curr = '      {}'.format(item)

            label = self.font.render(curr, 1, settings.FONT_COLOR)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (settings.SCREEN_WIDTH / 2) - (width / 2)
            totalHeight = len(settings.ITEMS) * height
            posy = (
                (settings.SCREEN_HEIGHT / 2)
                - (totalHeight / 2)
                + (index * height)
            )

            ret.append([label, (posx, posy)])
        return ret


# The menu class implements the main menu for the game, which can
# in turn navigate to the game, a future high score table once the
# scoring system is in place within the game, as well as quitting
# the application.

class Menu(object):
    """The scene containing the title screen and options."""

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game = Game(screen)
        self.menu_items = _MenuItems(self.game)
        self.running = True
        self.high_scores = HighScores(screen)

    def item_select(self, key):
        if key == pygame.K_UP:
            self.menu_items.prev()
        elif key == pygame.K_DOWN:
            self.menu_items.next()
        elif key == pygame.K_RETURN:
            if self.menu_items.current == MenuActions.GAME:
                if not self.game.game_over:
                    self.game.run()
                else:
                    self.game = Game(self.screen)
                    self.menu_items.game = self.game
                    self.game.run()
                self.game.run()
                self.high_scores.add_score(self.game.score_board.score)
            elif self.menu_items.current == MenuActions.HIGH_SCORES:
                self.high_scores.running = True
                self.high_scores.run()
            if self.menu_items.current == MenuActions.EXIT:
                self.running = False

    def run(self):
        """Run the menu.
        If the game is exited, the menu will continue running.
        If the menu is exited, then the game ends.
        """
        while self.running:
            # Limit frame speed to 60 FPS
            self.clock.tick(settings.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.item_select(event.key)

            # Redraw the background
            self.screen.fill(settings.BG_COLOR)

            for label, position in self.menu_items.render():
                self.screen.blit(label, position)

            pygame.display.flip()
        self.high_scores.save()
