"""Tests for the ships for our game."""
import unittest
from unittest import mock
import pygame
import random

from lazer_blast import settings
from lazer_blast.ships import (
    Enemy,
    Player,
)


class PlayerTestCase(unittest.TestCase):

    def setUp(self, surface=None):
        self.rand = random.Random()

    def test_set_momentum_moves_ship_on_update(self):
        player = Player()
        player.box = pygame.Rect(0, 0, 10, 10)
        player.surface = pygame.Surface((500, 500))
        player.momentum = (1, 0)
        ticks = self.rand.randint(3, 10)
        for i in range(ticks):
            next(player)
        expected = pygame.Rect(
            ticks * settings.SPEED,
            0, 10, 10
        )
        self.assertEqual(player.box, expected)

    def test_cannot_move_player_out_of_bounds(self):
        player = Player()
        player.surface = pygame.Surface((500, 500))
        player.box = pygame.Rect((0, 0, 100, 100))
        self.assertEqual(player.box, pygame.Rect((0, 0, 100, 100)))
        player.move(10, 10)
        self.assertEqual(
            player.box, pygame.Rect((10, 10, 100, 100)),
            'This should be legal!'
        )
        player.move(-20, -10)
        self.assertNotEqual(
            player.box, pygame.Rect((-10, 0, 100, 100)),
            'This should have been illegal, and readjusts',
        )
        self.assertEqual(
            player.box, pygame.Rect((0, 0, 100, 100)),
            'It should readjust to be in position'
        )

    def test_next_color_gets_next_in_list(self):
        player = Player()
        self.assertEqual(
            player.color,
            settings.COLORS[0],
            'The player should start out as the first color.'
        )
        player.next_color()
        self.assertEqual(
            player.color,
            settings.COLORS[1],
            'next_color should get the next color of all colors'
        )
        player.prev_color()
        self.assertEqual(
            player.color,
            settings.COLORS[0],
        )
        player.prev_color()
        self.assertEqual(
            player.color,
            settings.COLORS[-1],
            'prev color wraps around to the end.'
        )
        player.next_color()
        self.assertEqual(
            player.color,
            settings.COLORS[0],
        )


class EnemyTestCase(unittest.TestCase):

    def setUp(self, surface=None):
        self.rand = random.Random()

    def test_enemy_moves_from_top_to_bottom(self):
        enemy = Enemy()
        enemy.surface = pygame.Surface((500, 500))
        enemy.box = pygame.Rect(0, 0, 10, 10)
        ticks = self.rand.randint(3, 10)
        for i in range(ticks):
            next(enemy)
        expected = ticks * settings.ENEMY_SPEED
        self.assertEqual(
            enemy.box.top, expected,
            'The enemy should have moved down the screen.'
        )

    def test_in_bounds_method_tests_if_corner_is_in_bounds(self):
        enemy = Enemy()
        enemy.surface = pygame.Surface((500, 500))
        enemy.box = pygame.Rect(10, 0, 10, 10)
        self.assertTrue(
            enemy.in_bounds(),
            'The upper edge is in bounds.'
        )
        enemy.move(0, 400)
        self.assertTrue(
            enemy.in_bounds(),
            'In the middle is in bounds.'
        )
        enemy.move(0, 99)
        self.assertTrue(
            enemy.in_bounds(),
            'On the bottom edge is in bounds'
        )
        enemy.move(0, 2)
        self.assertFalse(
            enemy.in_bounds(),
            'Past the bottom is out of bounds'
        )

    @mock.patch('lazer_blast.ships.Random')
    def test_enemy_may_move_side_to_side(self, mock_random):
        rand = mock.MagicMock()
        mock_random.return_value = rand
        rand.random.return_value = 0.99
        enemy = Enemy(starting_pos=(50, 0), color=(255, 0, 0))
        enemy.surface = pygame.Surface((100, 100))
        self.assertEqual(
            enemy.box.left,
            50
        )
        next(enemy)
        self.assertEqual(
            enemy.box.left,
            50 + settings.ENEMY_SPEED,
            'If the random number is within bounds of 1.0 turns right.',
        )
        rand.random.return_value = 0.01
        next(enemy)
        self.assertEqual(
            enemy.box.left,
            50,
            'If the random number is within bounds of 0.0, turns left.',
        )
        rand.random.return_value = 0.5
        next(enemy)
        self.assertEqual(
            enemy.box.left,
            50,
            'If the random number is within bounds of 0.5, goes straight',
        )


class PlayerEnemyInteractionTestCase(unittest.TestCase):

    def test_player_knows_if_enemies_are_touching(self):
        surface = pygame.Surface((100, 100))
        player = Player()
        player.surface = surface
        player.box = pygame.Rect((45, 90, 10, 10))

        enemy1 = Enemy()
        enemy1.surface = surface
        enemy1.box = pygame.Rect((45, 0, 10, 10))
        enemy2 = Enemy()
        enemy2.surface = surface
        enemy2.box = pygame.Rect((55, 0, 10, 10))
        enemies = [enemy1, enemy2]

        self.assertFalse(
            player.enemies_touching(enemies),
            'No enemies should be touching the player.'
        )

        enemy1.box = pygame.Rect((50, 90, 10, 10))
        self.assertTrue(
            player.enemies_touching(enemies),
            'One enemy should be touching the player.',
        )
        enemy2.box = pygame.Rect((51, 90, 10, 10))
        self.assertTrue(
            player.enemies_touching(enemies),
            'Two enemies should be touching the player.',
        )
