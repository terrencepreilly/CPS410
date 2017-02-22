"""Tests for the ships for our game."""
import unittest
from unittest import mock
import pygame

from lazer_blast.base_classes import (
    ActorBase,
    RenderedBase,
    )


class PlayerTestCase(unittest.TestCase):
    def test_player_moves(self):
        self.assertTrue(False, 'Finish the test!')

    def test_player_stays_within_bounds(self):
        inputs = []
        ship = Player(world={})
        ship.(inputs)
        self.assertEqual(1, ship.get_rect.x)
        self.assertTrue(False, 'Finish the test!')


class EnemyTestCase(unittest.TestCase):
    def test_enemy_moves():
        self.assertTrue(False, 'Finish the test!')
    def test_enemy_stays_within_bounds(self):
        self.assertTrue(False, 'Finish the test!')

