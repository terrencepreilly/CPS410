# in globalvars.py
global playership
playership = []
# loads playership image
playership.append(
  load_file(DATADIR + 'pship.bmp')
  )
playership.append(
  load_file(DATADIR + 'pship1.bmp')
  )
playership.append(
  load_file(DATADIR + 'pship2.bmp')
  )
playership.append(
  load_file(DATADIR + 'pship3.bmp')
  )

# In player
def update(self):
  if self.state > 0:
    self.image = playership[
      self.state / explosion_speed
      ]
    self.state += 1
    if (self.state >= len(playership)
          * explosion_speed):
      self.state = 0
      self.image = playership[0]
