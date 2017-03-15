def __next__(self):
    """Get the next image to render to the screen.

    The action must first be set, and then next can be called upon it:
        some_actor = Actor()
        some_actor.set_action('walk')
        display(next(some_actor))

    Where Actor inherets RenderedBase, and display shows the returned
    image.
    """
    if self._action_i == -1:
        raise Exception('Action must be set')
    self._action_i += 1
    return self.images[self._action][self._action_i - 1]
