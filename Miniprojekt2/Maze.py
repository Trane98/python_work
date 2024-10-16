import pygame
import random
from main import create_grid_64x48
from main import draw_horizontal_water
from main import draw_vertical_water
from main import handle_event_exit
from queue import Queue

block_size = 10
grid = create_grid_64x48()

# Ramme til maze
draw_horizontal_water(grid, row=0, start_col=0, end_col=63)
draw_horizontal_water(grid, row=47, start_col=0, end_col=63)
draw_vertical_water(grid, col=63, start_row=0, end_row=47)

# Laver alle verticale linjer i mazen
for i in range(0, 62, 2):
    draw_vertical_water(grid, col=i, start_row=0, end_row=47)

# Laver en random maze
for i in range(2, 61, 2):
    random_numbers = random.randint(1, 46)
    grid[random_numbers][i] = 0

# BFS algoritme for at finde en sti fra start til slut
def bfs(grid, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        # Definerer retningerne for naboer (op, ned, venstre, højre)
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next = (current[0] + direction[0], current[1] + direction[1])

            # Kontrollerer, at vi er inde for grid, og om next er en gangbar celle (0)
            if 0 <= next[0] < len(grid) and 0 <= next[1] < len(grid[0]) and grid[next[0]][next[1]] == 0:
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current

    # Genopbygger stien
    current = goal
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

# Definerer start- og slutpunkter
start = (1, 1)
goal = (46, 62)

# Finder stien med BFS
path = bfs(grid, start, goal)

# Starter pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

running = True

while running:
    screen.fill((255, 255, 255))

    # Tegner labyrinten
    for row in range(48):
        for col in range(64):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (col * block_size, row * block_size, block_size, block_size))

    # Tegner stien fra BFS
    for pos in path:
        pygame.draw.rect(screen, (0, 255, 0), (pos[1] * block_size, pos[0] * block_size, block_size, block_size))

    pygame.display.flip()

    running = handle_event_exit()

pygame.quit()
