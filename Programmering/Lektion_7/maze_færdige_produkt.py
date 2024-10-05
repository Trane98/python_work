import pygame
import random
from main import create_grid_64x48
from main import draw_horizontal
from main import draw_vertical
from main import handle_event_exit

block_size = 10
grid = create_grid_64x48()


#Ramme til maze
draw_horizontal(grid, row=0, start_col=0, end_col=63)
draw_horizontal(grid, row=47, start_col=0, end_col=63)
draw_vertical(grid, col=63, start_row=0, end_row=47)

#Laver alle verticale linjer i mazen
for i in range(0, 62, 2):
    draw_vertical(grid, col=i, start_row=0, end_row=47)


#Laver en random maze, ved at ændre 1 værdier til 0 random hver anden gang, i takt med at alle blev lavet om til 1
#grid[row][col]
for i in range(2,61,2):
    random_numbers = random.randint(1,46)
    grid[random_numbers][i]=0

#Starter pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

running = True

while running:
    screen.fill((255,255,255))
    #Gennemgår hver celle i row og col og hvis værdierne er 1, så fylder den området med sort
    for row in range(48):
        for col in range(64):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (col * block_size, row * block_size, block_size, block_size))
            

    pygame.display.flip()

    running = handle_event_exit()

pygame.quit()