import pygame, sys
from queue import PriorityQueue

# Makes the grid 64x48
grid = [[0 for col in range(64)] for row in range(48)]

# The size for the pixels
cell_size = 10

# Colors
colors = {
    0: (30, 200, 30),  # Green - Grass
    1: (30, 30, 200),  # Blue - Water
    2: (125, 125, 125),  # Grey - Mountain
    "path": (255, 255, 0)  # Yellow - Path
}

# Starts pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Make key_state a start value which is grass
key_state = 0

# Stores the start and goal positions
start = None
goal = None

# Makes running true, for the while loop
running = True

def cost(current, next, grid):
    """Returns the cost of moving from current to next based on terrain."""
    terrain = grid[next[1]][next[0]]  # Get terrain from grid
    if terrain == 0:  # Grass
        return 1
    elif terrain == 1:  # Water
        return 3
    elif terrain == 2:  # Mountain
        return 5

def neighbors(current, grid):
    """Returns the valid neighbors of the current cell."""
    row, col = current
    neighbor_cells = []
    if row > 0:  # Move up
        neighbor_cells.append((row - 1, col))
    if row < len(grid) - 1:  # Move down
        neighbor_cells.append((row + 1, col))
    if col > 0:  # Move left
        neighbor_cells.append((row, col - 1))
    if col < len(grid[0]) - 1:  # Move right
        neighbor_cells.append((row, col + 1))
    return neighbor_cells

def pathfinding(start, goal, grid):
    """Performs the pathfinding algorithm using a priority queue."""
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in neighbors(current, grid):
            new_cost = cost_so_far[current] + cost(current, next, grid)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from

def reconstruct_path(came_from, start, goal):
    """Reconstructs the path from start to goal."""
    current = goal
    path = []
    
    while current != start:
        path.append(current)
        current = came_from[current]
    
    path.append(start)  # Optional: Add start to path
    path.reverse()  # Optional: Reverse path to be from start to goal
    return path

# Main game loop
while running:
    screen.fill((255, 255, 255))  # This is not important

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Registers the key which is pressed, activates the key, which makes the terrain different
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                key_state = 0
                print("Key 0 has been pressed, and its special ability has been activated")
            elif event.key == pygame.K_1:
                key_state = 1
                print("Key 1 has been pressed, and its special ability has been activated")
            elif event.key == pygame.K_2:
                key_state = 2
                print("Key 2 has been pressed, and its special ability has been activated")
            elif event.key == pygame.K_SPACE:
                # Run the pathfinding algorithm when space is pressed
                if start and goal:
                    came_from = pathfinding(start, goal, grid)
                    path = reconstruct_path(came_from, start, goal)
                    for (col, row) in path:
                        grid[row][col] = "path"  # Set path cells to yellow

        # Detects left mouse click [0] to set terrain or start/goal points
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()  # Gets the mouse position (x, y)
            col = pos[0] // cell_size  # Divided by cell_size
            row = pos[1] // cell_size  # Divided by cell_size

            # If right click is held down, set the start/goal points
            if pygame.key.get_pressed()[pygame.K_s]:  # Hold 'S' to set start
                start = (col, row)
                print(f"Start set at {start}")
            elif pygame.key.get_pressed()[pygame.K_g]:  # Hold 'G' to set goal
                goal = (col, row)
                print(f"Goal set at {goal}")
            else:
                # Updates the grid value, at the clicked position based on key_state
                grid[row][col] = key_state

            # ONLY FOR DEV, shares the values, what col, row and what value they have. This depends on the key_state
            print(f"Mouse clicked at grid position: (col={col}, row={row}) - Grid value changed to {key_state}")

    # Draw the grid
    for col in range(64):
        for row in range(48):
            color = colors[grid[row][col]]
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    pygame.display.flip()

pygame.quit()
