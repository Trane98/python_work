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

#Rect informations (starting point and box_size)
box_position = [370, 290]
box_size = [20, 20]

#Variabler til bevægelse
x = 0
y = 0

max_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()
    
    #Changing the movements of which and how keys are pressed
    if keys[pygame.K_a]:
        x -= 5
    if keys[pygame.K_d]:
        x += 5
    if keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_s]:
        y += 5


    if x > max_speed:
        x = max_speed
    elif x < -max_speed:
        x = -max_speed


    if y > max_speed:
        y = max_speed
    elif y < -max_speed:
        y = -max_speed



    box_position[0] += x
    box_position[1] += y



    #clear the screen
    screen.fill(WHITE)

    #Make rectangle
    pygame.draw.rect(screen, (BLACK), (box_position[0], box_position[1], box_size[0], box_size[1]))

    pygame.display.flip()
     
    # how many updates per second
    clock.tick(20)

pygame.quit()