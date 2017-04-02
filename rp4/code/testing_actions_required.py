def test_no_action_exception(self):
  pant = self.Pantomime()
  with self.assertRaises(Exception):
    pant.set_action('skeddadle')
