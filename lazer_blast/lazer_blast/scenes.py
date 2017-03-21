# This module contains scenes that can be updates interchangeably
# within the main loop of the game.

class Game(object):
  """ The scene containing gameplay. """
  def __init__(self):
    enemies = []
    player = None
    
  def update(self):
    """ Updates the scene and returns true if game is finished
        its execution. """
    return False

class Menu(object):
  """ The scene containing the title screen and options. """
  def __init__(self):
    pass

  def update(self):
    """ Updates the menu and returns true if menu is finished 
        its execution.  """
    return False
