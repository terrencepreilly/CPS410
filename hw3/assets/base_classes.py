# Terrence's section
class RenderedBase(object):
    images = dict()
    sounds = dict()
    _action = None
    _action_i = -1
    box = pygame.Rect(0, 0, 0, 0)

    def set_action(self, action):
        if action not in self.images:
            raise Exception
        self._action_i = 0
        self._action = action

    def __next__(self):
        if self._action_i == -1:
            raise Exception
        self._action_i += 1
        return self.images[self._action][self._action_i - 1]

    def render(self, context):
        pygame.draw.rect(context, (255, 0, 0), self.box)


class ActorBase(object):
    def __init__(self, health=0, weapons=list()):
        self.health = health
        self.weapons = weapons
        self._weapon_i = -1 if len(self.weapons) == 0 else 0

    def add_weapon(self, weapon):
        if self._weapon_i == -1:
            self._weapon_i = 0
        self.weapons.append(weapon)

    @property
    def weapon(self):
        if not (0 <= self._weapon_i < len(self.weapons)):
            raise Exception
        return self.weapons[self._weapon_i]

    def next_weapon(self):
        self._weapon_i = (self._weapon_i + 1) % len(self.weapons)
