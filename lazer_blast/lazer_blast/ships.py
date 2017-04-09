from random import Random
import pygame

from lazer_blast.base_classes import RenderedBase, ActorBase
from lazer_blast import settings


class Player(ActorBase, RenderedBase):
    """ Player's ship """

    # TODO: Brad's images go here
    images = {
        'box': [None, None],
    }

    def __init__(self, controls=dict(),
                 health=settings.PLAYER_HEALTH, weapons=list()):
        self.health = health
        self.weapons = weapons
        self._weapon_i = -1 if len(self.weapons) == 0 else 0
        self.controls = controls
        self.box = pygame.Rect(
            (settings.SCREEN_WIDTH / 2) - 25,
            settings.SCREEN_HEIGHT - 50,
            50,
            50
        )
        self.set_action('box')
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
                return True
        return False

    def flip_laser(self, state=None):
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
            # Render the laser
            pygame.draw.rect(context, self.color, self.laser)
        return super(Player, self).render(context)


class Enemy(ActorBase, RenderedBase):
    """ Enemy ship that combats player. """

    images = {
        'none': [None, None]
    }

    def __init__(self, health=settings.ENEMY_HEALTH,
                 color=(255, 0, 0, 255), starting_pos=(0, 0)):
        self.health = health
        self.weapons = list()
        self.color = color
        self.box = pygame.Rect(starting_pos[0], starting_pos[1], 50, 50)
        self.set_action('none')
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
    """ Graphic representation of a fired laserbeam. """

    def __init__(self, color=(0, 0, 0)):
        self.color = color
