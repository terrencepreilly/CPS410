class Pantomime(RenderedBase):
  images = {
      'walk': ['fake_walk_{}'.format(x)
               for x in range(10)],
      'run': ['fake_run_{}'.format(x)
              for x in range(10)],
  }
  sounds = {
      'bump': 'fake_bump'
  }
