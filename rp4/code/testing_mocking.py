def test_render_called_with_box(
        self, mock_draw):
  surface = pygame.Surface(
      (1000, 1000)
  )
  rb = RenderedBase()
  rb.render(surface)
  self.assertEqual(
      mock_draw.call_count, 1
  )
  positional, _ = mock_draw.call_args
  self.assertEqual(
      positional[2],
      rb.box,
  )
