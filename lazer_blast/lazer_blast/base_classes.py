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
    surface = pygame.Surface((0, 0))
    color = (255, 0, 0, 0)

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
        if self._action_i == len(self.images[self._action]):
            self._action_i = 0
        return self.images[self._action][self._action_i - 1]

    def render(self, context):
        """This should probably be updated once we have images."""
        pygame.draw.rect(context, self.color, self.box)

    def move(self, x, y):
        self.box = self.box.move(x, y)

    def in_bounds(self):
        """Return True if this actor is within the bounds of the surface"""
        return self.surface.get_bounding_rect().contains(self.box) == 1


class ActorBase(object):
    """Implements basic attributes of an actor."""

    def __init__(self, health=0, weapons=list()):
        self.health = health
        self.weapons = weapons
        self._weapon_i = -1 if len(self.weapons) == 0 else 0
        # Also holds bounds information
        self._position = pygame.Rect((0, 0, 100, 100))

    def add_weapon(self, weapon):
        """Adds a weapon to this actor's arsenal."""
        if self._weapon_i == -1:
            self._weapon_i = 0
        self.weapons.append(weapon)

    @property
    def weapon(self):
        """Get the current weapon for this player."""
        if not (0 <= self._weapon_i < len(self.weapons)):
            raise Exception('No weapons')
        return self.weapons[self._weapon_i]

    def next_weapon(self):
        """Switch to the next weapon."""
        self._weapon_i = (self._weapon_i + 1) % len(self.weapons)
