import pygame, sys
from main import handle_event_exit

grid_64x48 = [[0 for col in range(64)] for row in range(48)]

grid = grid_64x48
block_size = 10


keys = pygame.key.get_pressed
pygame.mouse.get_pressed

#Starter pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

running = True



while running:
    screen.fill((255,255,255))

    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed():
        



            

    pygame.display.flip()

    running = handle_event_exit()

pygame.quit()