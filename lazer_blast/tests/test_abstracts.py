"""Tests for the abstract base classes for our game."""
import unittest
from unittest import mock
import pygame

from lazer_blast.base_classes import (
    RenderedBase,
    )


class RenderedBaseTestClass(unittest.TestCase):
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
