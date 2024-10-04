import pygame
from main import create_grid_64x48
from main import draw_horizontal
from main import draw_vertical

block_size = 10
grid = create_grid_64x48()


#Ramme til maze
draw_vertical(grid, row=0, start_col=0, end_col=63)
draw_vertical(grid, row=47, start_col=0, end_col=63)
draw_horizontal(grid, col=0, start_row=0, end_row=47)
draw_horizontal(grid, col=63, start_row=0, end_row=47)

for i in range(0, 11, 2):
    draw_vertical(grid, row=i, start_col=0, end_col=63)

pygame.init()
screen = pygame.display.set_mode((640, 480))


while True:
    screen.fill((255,255,255))

    for row in range(48):
        for col in range(64):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (col * block_size, row * block_size, block_size, block_size))





    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()