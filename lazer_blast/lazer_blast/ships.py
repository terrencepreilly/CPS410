import os
from random import Random
import pygame

from lazer_blast.base_classes import RenderedBase, ActorBase
from lazer_blast import settings


class Player(ActorBase, RenderedBase):
    """ Player's ship """

    images = {
        'fly': [
            pygame.image.load(os.path.join(settings.BASE_DIR, x))
            for x in ['assets/player.png']
        ],
    }

    def __init__(self, controls=dict(),
                 health=settings.PLAYER_HEALTH, weapons=list()):
        self.health = health
        self.weapons = weapons
        self._weapon_i = -1 if len(self.weapons) == 0 else 0
        self.controls = controls
        self.set_action('fly')
        self.box = self.images['fly'][0].get_rect()
        self.box.left = settings.SCREEN_WIDTH / 2 - 25
        self.box.top = settings.SCREEN_HEIGHT - 50
        self.color_i = 0
        self.color = settings.COLORS[self.color_i]
        self._laser = False
        self.laser = pygame.Rect((
            self.box.left + (0.5 * self.box.width) - 3,
            self.box.top - settings.SCREEN_HEIGHT,
            3,
            settings.SCREEN_HEIGHT,
        ))

        # Describes how fast the player is moving in a given direction.
        self.momentum = (0, 0)

    def move(self, x, y):
        super(Player, self).move(x, y)
        if not self.in_bounds():
            height = self.surface.get_bounding_rect().height
            width = self.surface.get_bounding_rect().width
            diffx = 0
            if self.box.left < 0:
                diffx = - self.box.left
            elif self.box.right > width:
                diffx = width - self.box.right
            diffy = 0
            if self.box.top < 0:
                diffy = - self.box.top
            elif self.box.bottom > height:
                diffy = height - self.box.bottom
            self.box = self.box.move(diffx, diffy)
        self.laser.left = self.box.left + (0.5 * self.box.width) - 3
        self.laser.top = self.box.top - settings.SCREEN_HEIGHT

    def _update_position(self):
        """Update the Player's position."""
        self.move(*(x * settings.SPEED for x in self.momentum))

    def __next__(self):
        """Update the position, and return the next image in the
        sequence for this action."""
        self._update_position()
        return super(Player, self).__next__()

    def next_color(self):
        """Switch to the next color laser."""
        self.color_i += 1
        if self.color_i >= len(settings.COLORS):
            self.color_i = 0
        self.color = settings.COLORS[self.color_i]

    def prev_color(self):
        """Switch to the previous color laser."""
        self.color_i -= 1
        if self.color_i < 0:
            self.color_i = len(settings.COLORS) - 1
        self.color = settings.COLORS[self.color_i]

    def enemies_touching(self, enemies):
        """Return True if any of the given enemies is touching this player."""
        # We don't use collidelist() because we would have to gather
        # all of the rects first.  This way we short-circuit.
        for enemy in enemies:
            if self.box.colliderect(enemy.box):
                Player.PlaySound(
                    self, "367622__fxkid2__explosion-with-debris.wav")
                return True
        return False

    def flip_laser(self, state=None):
        self.PlaySound("42106__marcuslee__laser-wrath-4.wav")
        """Changes the state of the laser (on/off).
        Args:
            state: An optional state argument (True or False).
                If None, the laser will switch states.
        """
        if state is None:
            self._laser = not self._laser
        else:
            # Make sure that _laser is a boolean value
            self._laser = bool(state)

    def render(self, context):
        if self._laser:
            pygame.draw.line(
                context,
                self.color,
                (self.box.x + (0.5 * self.box.width) - 3, self.box.y),
                (self.box.x + (0.5 * self.box.width) - 3, self.laser.top),
                3
            )
        return super(Player, self).render(context)

    def PlaySound(self, file):
        assets_path = os.path.join(settings.BASE_DIR, "assets")
        sound_path = os.path.join(assets_path, file)
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()


class Enemy(ActorBase, RenderedBase):
    """ Enemy ship that combats player. """

    images = dict()

    possible_images = {
        x: pygame.image.load(
            os.path.join(
                settings.BASE_DIR,
                'assets/enemy_{}_1.png'.format(x)
            )
        )
        for x in ['red', 'green', 'blue']
    }

    def _set_images(self):
        """Since the color is dynamic at creation, the image is, too."""
        try:
            color = settings.COLOR_LOOKUP[self.color]
        except KeyError:
            color = 'red'
        self.images = {'fly': [self.possible_images[color]]}

    def __init__(self, health=settings.ENEMY_HEALTH,
                 color=settings.COLORS[0], starting_pos=(0, 0)):
        self.health = health
        self.weapons = list()
        self.color = color
        self.box = pygame.Rect(starting_pos[0], starting_pos[1], 50, 50)
        self._set_images()
        self.set_action('fly')
        self.momentum = (0, 1)
        self.rand = Random()
        # Target (player) must be set or enemy will not take damage
        self.target = None

    def _update_position(self):
        """Update the Player's position."""
        dx = self.momentum[0]
        r = self.rand.random()
        if 0 <= r <= settings.TURN_BOUND:
            dx = -1
        elif 0.5 - settings.TURN_BOUND <= r <= 0.5 + settings.TURN_BOUND:
            dx = 0
        elif 1 - settings.TURN_BOUND <= r <= 1:
            dx = 1
        self.momentum = (dx, 1)
        self.move(*(x * settings.ENEMY_SPEED for x in self.momentum))

    def _is_hit(self):
        if self.target is None:
            return False
        return (self.target._laser
                and bool(self.target.laser.colliderect(self.box))
                and self.color == self.target.color)

    def _update_health(self):
        if self._is_hit():
            self.health -= settings.PLAYER_STRENGTH

    def __next__(self):
        """Update the position, and return the next image in the
        sequence for this action."""
        self._update_position()
        self._update_health()
        return super(Enemy, self).__next__()

    def in_bounds(self):
        """Return True if this actor is within the bounds of the surface"""
        return self.surface.get_bounding_rect().collidepoint(
            self.box.topleft) == 1


class LaserBlaster(object):
    """ A weapon for ships to use. """

    def __init__(self, color=(0, 0, 0), charge=0, damage=0):
        self.color = color
        self.charge = charge
        self.damage = damage


class LaserBeam(RenderedBase):
    """ Graphic representation of a fired laserbeamSRA. """

    def __init__(self, color=(0, 0, 0)):
        self.color = color


class HealthBar(RenderedBase):

    def __init__(self, color=(0, 255, 0), player=None):
        self.color = color
        self.box = pygame.Rect(
            settings.SCREEN_WIDTH * 0.25,
            settings.SCREEN_HEIGHT - 10,
            settings.SCREEN_WIDTH * 0.5,
            5,
        )
        self.player = player

    def __next__(self):
        """Updates for width to match the player's health."""
        if self.player is None:
            return
        percent = self.player.health / settings.PLAYER_HEALTH
        self.box.width = percent * settings.SCREEN_WIDTH * 0.5


class ScoreBoard(RenderedBase):

    def __init__(self, color=(255, 255, 255)):
        self.color = color
        self.font = pygame.font.SysFont(
            settings.FONT,
            settings.FONT_SIZE,
        )
        self.score = 0

    def add_points(self, amount=1):
        self.score += amount

    def _render_score(self):
        return 'Score: {}'.format(self.score * 10)

    def render(self, context):
        """This should probably be updated once we have images."""
        label = self.font.render(self._render_score(), 1, settings.FONT_COLOR)

        width = label.get_rect().width
        height = label.get_rect().height

        if width > 50:
            posx = settings.SCREEN_WIDTH - width - 10
        else:
            posx = settings.SCREEN_WIDTH - 50

        posy = (
            settings.SCREEN_HEIGHT
            - height
            - 5
        )
        context.blit(label, (posx, posy))
