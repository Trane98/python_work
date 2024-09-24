import pygame
import math

pygame.init() # Initialize Pygame
screen_size = (640,480)
screen = pygame.display.set_mode(screen_size) # Create a window of 840x680 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

box_position=(screen_size[0]//2, screen_size[1]//2)
box_size=(5,5)

for angle in range(0,360*5,5):
    r=0.1*angle
    x=r*math.cos(math.radian(angle))
    y=r*math.sin(math.radians(angle))
    current_position=(box_position[0]+x, box_position[1]+y)
    pygame.draw.rect(screen,(0,0,0)), current_position+box_size





# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears