   #LazerStrike class will display a laser object of a specific color 
   #when a certain key is selected. If the laser is of the same color as 
   #the enemy target and makes contact, then this class will call the     
   #GameSound() class in order to implement the crashing sound that will   
   #return from a direct hit. This class will also call the Enemy() class 
   #in order to deduct health upon a hit. 
import pygame, sys

pygame.init()

(width, height) = (700, 500)
color = pygame.event.get()
stat = ""
screen = pygame.display.set_mode((width, height), 0, 32)
start_pos = (350, 470)
end_pos = (350, 100)


laser_color = ""

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)

gameEnd = False

while not gameEnd:

    for color in pygame.event.get():
        if color.type == pygame.QUIT:
            sys.exit()
            gameEnd = True
        if color.type == pygame.KEYDOWN:
            if color.key == pygame.K_w:
                pygame.draw.line(screen, red, start_pos, end_pos, 3)
            elif color.key == pygame.K_a:
                pygame.draw.line(screen, green, start_pos, end_pos, 3)  
            elif color.key == pygame.K_d:
                pygame.draw.line(screen, blue, start_pos, end_pos, 3)
            elif color.key == pygame.K_s:
                pygame.draw.line(screen, yellow, start_pos, end_pos, 3)
            else:
                pygame.draw.line(screen, white, start_pos, end_pos, 3)
        if color.type == pygame.KEYUP:
            #add logic to hide laser (unsure if this would work)
            #could check if the line is black and do no damage/penalty
            pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 3)
            
    pygame.display.update()
