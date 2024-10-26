import pygame
import sys
from queue import Queue

# Makes the grid 64x48
grid = [[0 for col in range(64)] for row in range(48)]

# The size for the pixels
cell_size = 10

# Colors
colors = {
    0: (30, 200, 30),  # Green
    1: (125, 125, 125),  # Gray
    "path": (255, 255, 0)  # Yellow
}

# Set start and goal positions
start = (1, 1)  # Starting position as a tuple
goal = (62, 46)  # Goal position as a tuple

# Start pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Make key_state a start value which is grass
key_state = 0
path = []  # Initialize path variable
path_found = False  # Flag to track if path is found

# Function to find neighbors in the grid
def graph_neighbors(x, y):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Check if within bounds and if cell is passable
        if 0 <= nx < 64 and 0 <= ny < 48 and grid[ny][nx] == 0:
            neighbors.append((nx, ny))
    
    return neighbors

# Function to perform BFS and return the path
def bfs(start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break  # Stop if goal is reached
        
        for next in graph_neighbors(current[0], current[1]):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    # Reconstruct path from goal to start
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()  # Optional to start from `start` to `goal`
    return path

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Registers key to toggle terrain types
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                key_state = 0
            elif event.key == pygame.K_1:
                key_state = 1
            elif event.key == pygame.K_SPACE:
                # Trigger BFS when the space key is pressed
                path = bfs(start, goal)
                path_found = True

        # Detects left mouse click to change terrain
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            col = pos[0] // cell_size
            row = pos[1] // cell_size
            grid[row][col] = key_state

    # Draws the grid
    for col in range(64):
        for row in range(48):
            color = colors[grid[row][col]]
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    # Draw the path in yellow if found
    if path_found:
        for (x, y) in path:
            pygame.draw.rect(screen, colors["path"], (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.display.flip()

pygame.quit()
