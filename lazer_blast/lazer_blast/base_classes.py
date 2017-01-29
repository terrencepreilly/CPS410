import pygame


class RenderedBase(object):
    """Represents an object which can be rendered to the screen.

    Movements should be implemented in the subclass.
    """

    # The images should map a given action (as a String)
    # to a list of images.
    images = dict()

    # Should map a given action/event as a String
    # to a single sound.
    sounds = dict()

    # The current action being performed.
    _action = None
    _action_i = -1

    # The bounding box for this figure
    box = pygame.Rect(0, 0, 0, 0)

    def set_action(self, action):
        """Set the current action for this renderable object."""
        if action not in self.images:
            raise Exception('Action not defined for {}'.format(
                self.__name__
                ))
        self._action_i = 0
        self._action = action

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

    def render(self, context):
        pygame.draw.rect(context, (255, 0, 0), self.box)
