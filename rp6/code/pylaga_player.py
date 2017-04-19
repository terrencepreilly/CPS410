def shoot(self, shotslist, locx, locy):
  self.boom = Bullet(shotslist)
  self.boom.set_pos(locx, locy)
  shotslist.add(self.boom)
