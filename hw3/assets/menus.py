#Keefer's section
class MainMenu():
    def __init__(self, cursor=0):
        #set the menu type (main/high score/options)

        self.setup_graphic()
        self.setup_cursor()

    def setup_graphic(self):
        #draw title graphic/high score table

    def setup_cursor(self):
        self.cursor = cursor
        #draw cursor image

    def update_cursor(self, keys):
        if self.cursor.state == 0:
            #Point to option one (New Game/Set buttons/Return)
            if key down:
                self.cursor.state == 1
            elif key return:
                #Initialize new game/set keys/return to previous
        elif self.cursor.state == 1:
            #Point to option two (High Scores/return)
            if key down:
                self.cursor.state == 2
            elif key up:
                self.cursor.state == 0
            elif key return:
                #Initialize options menu
        elif self.cursor.state == 2:
            #Point to option three (Exit)
            if key down:
                self.cursor.state == 3
            elif key up:
                self.cursor.state == 2
            elif key return:
                #open options menu
        elif self.cursor.state == 3:
            #Point to option three (Exit)
            if key up:
                self.cursor.state == 2
            elif key return:
                #close the application
