import pygame
from base_classes import RenderedBase, ActorBase

class Player(ActorBase, RenderedBase):
    """ Player's ship """
    def __init__(self, controls=dict(), health=0, weapons=list()):
        ActorBase.__init__(health=health, weapons=weapons)
        self.controls = controls

class Enemy(ActorBase, RenderedBase):
    """ Enemy ship that combats player. """
    def __init__(self, health=0, weapons=list()):
        ActorBase.__init__(health=health, weapons=weapons)

class LaserBlaster(object):
    """ A weapon for ships to use. """
    def __init__(self, color=(0,0,0), charge=0, damage=0):
        self.color = color
        self.charge = charge
        self.damage = damage

class LaserBeam(RenderedBase):
    """ Graphic representation of a fired laserbeam. """
    def __init__(self, color=(0,0,0)):
        self.color = color

