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

    @mock.patch('lazer_blast.ships.pygame.mixer')
    @mock.patch('lazer_blast.ships.os')
    def test_set_momentum_moves_ship_on_update(self, mock_os, mock_mixer):
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

    @mock.patch('lazer_blast.ships.pygame.mixer')
    @mock.patch('lazer_blast.ships.os')
    def test_cannot_move_player_out_of_bounds(self, mock_os, mock_mixer):
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

    @mock.patch('lazer_blast.ships.pygame.mixer')
    @mock.patch('lazer_blast.ships.os')
    def test_next_color_gets_next_in_list(self, mock_os, mock_mixer):
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

    @mock.patch('lazer_blast.ships.pygame.mixer')
    @mock.patch('lazer_blast.ships.os')
    @mock.patch('lazer_blast.ships.pygame.draw.rect')
    def test_when_laser_on_rect_drawn(self, mock_draw, mock_os, mock_mixer):
        player = Player()
        player.box = pygame.Rect(0, 0, 10, 10)
        player.surface = pygame.Surface((500, 500))
        player.render(player.surface)
        self.assertEqual(mock_draw.call_count, 0)
        player.flip_laser()
        self.assertTrue(player._laser)
        player.render(player.surface)
        self.assertEqual(
            mock_draw.call_count,
            1,
            'It should have called once for the player, '
            'And one more time for the laser shape. '
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

    def test_enemy_takes_damage_when_hit(self):
        surface = pygame.Surface((100, 100))
        enemy = Enemy()
        enemy.surface = surface
        enemy._is_hit = lambda: True
        next(enemy)
        self.assertEqual(
            settings.ENEMY_HEALTH - settings.PLAYER_STRENGTH,
            enemy.health,
        )


class PlayerEnemyInteractionTestCase(unittest.TestCase):

    def setUp(self):
        color = (255, 0, 0)
        surface = pygame.Surface((100, 100))
        self.player = Player()
        self.player.surface = surface
        self.player.box = pygame.Rect((45, 90, 10, 10))
        self.player.color = color

        enemy1 = Enemy()
        enemy1.color = color
        enemy1.surface = surface
        enemy1.box = pygame.Rect((45, 0, 10, 10))
        enemy1.target = self.player
        enemy2 = Enemy()
        enemy2.color = color
        enemy2.surface = surface
        enemy2.box = pygame.Rect((55, 0, 10, 10))
        enemy2.target = self.player
        self.enemies = [enemy1, enemy2]

    def test_player_knows_if_enemies_are_touching(self):
        enemy1, enemy2 = self.enemies
        self.assertFalse(
            self.player.enemies_touching(self.enemies),
            'No enemies should be touching the player.'
        )

        enemy1.box = pygame.Rect((50, 90, 10, 10))
        self.assertTrue(
            self.player.enemies_touching(self.enemies),
            'One enemy should be touching the player.',
        )
        enemy2.box = pygame.Rect((51, 90, 10, 10))
        self.assertTrue(
            self.player.enemies_touching(self.enemies),
            'Two enemies should be touching the player.',
        )

    def test_enemy_takes_damage_from_lazer_only(self):
        self.player.flip_laser(True)
        enemy1, enemy2 = self.enemies

        enemy1.box.left = self.player.laser.left
        enemy1.box.top = self.player.laser.top + 20

        # half-way overlapping with player (below)
        enemy2.box.left = self.player.box.left
        enemy2.box.top = self.player.box.top + 5

        self.assertEqual(enemy1.health, settings.ENEMY_HEALTH)
        self.assertEqual(enemy2.health, settings.ENEMY_HEALTH)

        next(enemy1)
        next(enemy2)

        self.assertEqual(
            enemy1.health,
            settings.ENEMY_HEALTH - settings.PLAYER_STRENGTH
        )
        self.assertEqual(enemy2.health, settings.ENEMY_HEALTH)

    def test_enemy_doesnt_take_damage_from_inactive_laser(self):
        self.player.flip_laser(False)
        enemy = self.enemies[0]

        enemy.box.left = self.player.laser.left
        enemy.box.top = self.player.laser.top + 20

        next(enemy)

        self.assertEqual(enemy.health, settings.ENEMY_HEALTH)
