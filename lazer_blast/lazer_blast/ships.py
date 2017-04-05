import pygame

from lazer_blast.base_classes import RenderedBase, ActorBase
from lazer_blast import settings


class Player(ActorBase, RenderedBase):
    """ Player's ship """

    # TODO: Brad's images go here
    images = {
        'box': [None, None],
    }

    def __init__(self, controls=dict(), health=0, weapons=list()):
        self.health = health
        self.weapons = weapons
        self._weapon_i = -1 if len(self.weapons) == 0 else 0
        self.controls = controls
        self.position = (0, 0)
        self.box = pygame.Rect(0, 0, 50, 50)
        self.set_action('box')

        # Describes how fast the player is moving in a given direction.
        self.momentum = (0, 0)

    def _update_position(self):
        """Update the Player's position."""
        self.move(*(x * settings.SPEED for x in self.momentum))

    def __next__(self):
        """Update the position, and return the next image in the
        sequence for this action."""
        self._update_position()
        return super(Player, self).__next__()


class Enemy(ActorBase, RenderedBase):
    """ Enemy ship that combats player. """

    def __init__(self, health=0, weapons=list()):
        ActorBase.__init__(health=health, weapons=weapons)


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
