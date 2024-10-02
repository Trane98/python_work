import pygame , sys
from datetime import datetime
import math
import pygame.key
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (840, 680)
 
# create a window
screen = pygame.display.set_mode(screen_size)
 
# clock is used to set a max fps
clock = pygame.time.Clock()

box_position = [370, 290]
box_size = [20, 20]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    #Changing the movements of which and how keys are pressed
    if keys[pygame.K_a]:
        box_position[0] -= 5
    if keys[pygame.K_d]:
        box_position[0] += 5
    if keys[pygame.K_w]:
        box_position[1] -= 5
    if keys[pygame.K_s]:
        box_position[1] += 5

    #clear the screen
    screen.fill(WHITE)

    #Make rectangle
    pygame.draw.rect(screen, (BLACK), (box_position[0], box_position[1], box_size[0], box_size[1]))

    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)

pygame.quit()