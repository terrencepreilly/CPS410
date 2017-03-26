#The menu class implements the main menu for the game, which can
#in turn navigate to the game, a future high score table once the
#scoring system is in place within the game, as well as quitting
#the application.
 
import pygame
pygame.init()

class Menu():
    def __init__(self, screen, items, bg_color=(0,0,0), font='Arial', font_size=30, font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.items = items
        self.new_items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

        self.cur_item = 0
 
        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            totalHeight = len(items) * height
            posy = (self.scr_height / 2) - (totalHeight / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])

    def item_select(self, key):
        #Items chosen with up/down, selected with space bar
        if self.cur_item is None:
            self.cur_item = 0
        else:
            #on keystroke, reassign selected option
            if key == pygame.K_UP and self.cur_item > 0:
                self.cur_item -= 1
                if self.cur_item == 0:
                    self.new_items = ('> Start Game', '   High Scores', '   Quit')
                elif self.cur_item == 1:
                    self.new_items = ('   Start Game', '> High Scores', '   Quit')
            elif key == pygame.K_DOWN and self.cur_item < len(self.items)-1:
                self.cur_item += 1
                if self.cur_item == 1:
                    self.new_items = ('   Start Game', '> High Scores', '   Quit')
                elif self.cur_item == 2:
                    self.new_items = ('   Start Game', '   High Scores', '> Quit')
            #space bar performs an action
            elif key == pygame.K_SPACE:
                if self.cur_item == 0:
                    #MOVE TO THE GAME SCENE FROM THIS OPTION
                    print("Starting game...")
                elif self.cur_item == 1:
                    #LOAD THE HIGH SCORE TABLE ONCE SCORING HAS BEEN IMPLEMENTED
                    print("Loading high scores...")
                elif self.cur_item == 2:
                    #QUIT THE GAME
                    print("Quitting application...")
                    pygame.quit()

        self.items = []
        for index, item in enumerate(self.new_items):
            label = self.font.render(item, 1, self.font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            totalHeight = len(self.new_items) * height
            posy = (self.scr_height / 2) - (totalHeight / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])
            
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 60 FPS
            self.clock.tick(60)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                   self.item_select(event.key)
 
            # Redraw the background
            self.screen.fill(self.bg_color)
 
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
 
            pygame.display.flip()
 
 
if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((800, 600), 0, 32)

    pygame.display.set_caption('Lazer Blast!')
    menu_items = ('> Start Game', '   High Scores', '   Quit')
 
    gm = Menu(screen, menu_items)
    gm.run()
