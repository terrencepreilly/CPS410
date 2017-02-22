# Meagon's Section
class GameSound(string):
    sounds = dict()

    if string == 'fire':
        sounds = dict['fire']
    elif string == 'hit':
        sounds = dict['hit']
    else:
        error
    sounds = none
    sounds.play()


class ShipProjectile(stringC, stringT):

    Color = ''
    Type = ''
    JAMMED = error

    def __init__(self, color, type):
        self.color = color
        self.type = type

    def projectileColor(stringC):
        if stringC == 'blue':
            color = stringC
        elif stringC == 'red':
            color = stringC
        elif stringC == 'green':
            color = string
        else:
            color = 'white'  # default color, no hit points

    def projectileType(stringT):
        if stringT == 'enemy':
            Type = stringT
        elif stringT == 'player':
            Type = stringT
        else:
            Type = 'JAMMED'  # default, no fire of projectile

        missile = ShipProjectile(stringC, stringT)
        return missile
