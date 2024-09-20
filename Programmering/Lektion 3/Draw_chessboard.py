import pygame
import math

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((840, 680)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

for i in range(1,11):
    firkant=pygame.draw.rect(screen, (0,0,0),(i*50,50,25,25))







# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears