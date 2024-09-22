import pygame
import math

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((840, 680)) # Create a window of 840x680 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

for lige_tal in range(0,7,2):#Koden her sørger for at tallene ganges med 0,2,4,6
    for ulige_tal in range(1,8,2):#Koden her sørger for at tallene ganges med 1,3,5,7
        for interval_mellem_1_og_5 in range(1,5): #Koden her sørger for at vi ganger i intervallet 1,2,3,4
            firkant=pygame.draw.rect(screen, (0,0,0),(lige_tal*25,ulige_tal*25,25,25))
            firkant=pygame.draw.rect(screen, (0,0,0),(ulige_tal*25,interval_mellem_1_og_5*50,25,25))

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears