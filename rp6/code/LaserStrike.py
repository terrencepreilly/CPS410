class LaserStrike(object):

  def _init_(self, color):
    self.color = color

  def enemy_color(self, enemy_color):
    if self.color == enemy_color:
      GameSound.hit()
