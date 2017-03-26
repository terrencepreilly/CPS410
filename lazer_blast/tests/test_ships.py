"""Tests for the ships for our game."""
import unittest
import pygame
import random

from lazer_blast import settings
from lazer_blast.ships import (
    Player,
    )


class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.rand = random.Random()

    def test_set_momentum_moves_ship_on_update(self):
        player = Player()
        player.box = pygame.Rect(0, 0, 0, 0)
        player.momentum = (1, 0)
        ticks = self.rand.randint(3, 100)
        for i in range(ticks):
            next(player)
        expected = pygame.Rect(
            ticks * settings.SPEED,
            0, 0, 0
            )
        self.assertEqual(player.box, expected)


class EnemyTestCase(unittest.TestCase):

    def test_enemy_moves(self):
        self.assertTrue(False, 'Finish the test!')

    def test_enemy_stays_within_bounds(self):
        self.assertTrue(False, 'Finish the test!')
