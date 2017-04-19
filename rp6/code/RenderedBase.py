def __next__(self):
  if self._action_i == -1:
    raise Exception('Action must be set')
  self._action_i += 1
  return self.images[self._action][
    self._action_i-1
    ]
