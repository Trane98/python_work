import pygame
import math

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((840, 680)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white


x_start, y_start=420, 340
længde=200
bredde=4

for i in range(1,13):
    angle=math.radians(i*30)
    x_end=x_start+længde*math.cos(angle)
    y_end=y_start+længde*math.sin(angle)
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)






# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears