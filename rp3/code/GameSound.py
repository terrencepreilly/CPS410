class GameSound(object):

  def _play(self, sound):
    def inner():
      pygame.mixer.init()
      pygame.mixer.music.load(sound)
      pygame.mixer.music.play()
    return inner

  fire = _play('laserFire.wav')
  hit = _play('directHit.wav')
  win = _play('playerWon.wav')
  lose = _play('playerLost.wav')
