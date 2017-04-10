"""Tests for the abstract base classes for our game."""
import unittest
from unittest import mock
import pygame

from lazer_blast.base_classes import (
    ActorBase,
    RenderedBase,
)


class RenderedBaseTestCase(unittest.TestCase):
    # A fake subclass

    class Pantomime(RenderedBase):
        images = {
            'walk': ['fake_walk_{}'.format(x) for x in range(10)],
            'run': ['fake_run_{}'.format(x) for x in range(10)],
        }
        sounds = {
            'bump': 'fake_bump'
        }

    def test_has_images(self):
        rb = RenderedBase()
        self.assertTrue(isinstance(rb.images, dict))

    @unittest.skip('Why is this here?  Sounds don\'t appear to be used.')
    def test_has_sound(self):
        rb = RenderedBase()
        self.assertTrue(isinstance(rb.sounds, dict))

    def test_subclass_can_access_sequence_of_images(self):
        pant = self.Pantomime()

        pant.set_action('walk')
        self.assertEqual(next(pant), 'fake_walk_0')
        self.assertEqual(next(pant), 'fake_walk_1')
        self.assertEqual(next(pant), 'fake_walk_2')

        pant.set_action('run')
        self.assertEqual(next(pant), 'fake_run_0')

    def test_not_setting_action_raises_exception(self):
        pant = self.Pantomime()
        with self.assertRaises(Exception):
            next(pant)

    def test_undefined_action_raises_exception(self):
        pant = self.Pantomime()
        with self.assertRaises(Exception):
            pant.set_action('skeddadle')

    def test_bounding_box_defined(self):
        rb = RenderedBase()
        self.assertTrue(isinstance(rb.box, pygame.Rect))

    @mock.patch('lazer_blast.base_classes.pygame.draw.rect')
    def test_render_called_with_box(self, mock_draw):
        surface = pygame.Surface((1000, 1000))
        rb = RenderedBase()
        rb.render(surface)
        self.assertEqual(mock_draw.call_count, 1)
        positional, _ = mock_draw.call_args
        self.assertEqual(
            positional[2],
            rb.box,
        )

    def test_in_bounds(self):
        rb = RenderedBase()
        rb.box = pygame.Rect((0, 0, 100, 100))
        rb.surface = pygame.Surface((500, 500))
        self.assertTrue(rb.in_bounds())
        rb.box = pygame.Rect((-100, -100, -50, -50))
        self.assertFalse(rb.in_bounds())
        rb.box = pygame.Rect((-100, 100, -50, 50))
        self.assertFalse(rb.in_bounds())
        rb.box = pygame.Rect((500, 500, 600, 600))
        self.assertFalse(rb.in_bounds())


class ActorBaseTestCase(unittest.TestCase):

    def test_actor_base_has_health(self):
        actor = ActorBase()
        self.assertTrue(isinstance(actor.health, int))

    def test_actor_can_have_weapons(self):
        actor = ActorBase()
        self.assertTrue(isinstance(actor.weapons, list))

    def test_can_add_weapons_to_actor(self):
        weapon1, weapon2 = 'A fake weapon', 'Another fake weapon'
        actor = ActorBase(100, [weapon1])
        self.assertEqual(actor.weapon, weapon1)
        actor.add_weapon(weapon2)
        actor.next_weapon()
        self.assertEqual(actor.weapon, weapon2)
        actor.next_weapon()
        self.assertEqual(actor.weapon, weapon1)

    def test_single_weapon_never_changes(self):
        weapon1 = 'A fake weapon'
        actor = ActorBase(100, [weapon1])
        actor.add_weapon(weapon1)
        self.assertEqual(actor.weapon, weapon1)
        actor.next_weapon()
        self.assertEqual(actor.weapon, weapon1)
