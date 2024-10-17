import pygame, sys
from queue import Queue

# Makes the grid 64x48
grid = [[0 for col in range(64)] for row in range(48)]

# The size for the pixels
cell_size = 10

# Colors
colors = {
    0: (30, 200, 30),  # Green
    1: (30, 30, 200),  # Blue
    2: (125, 125, 125),  # Grey
    'path': (255, 255, 0)  # Yellow for the path
}

# Get neighbors function to return valid neighboring cells (up, down, left, right)
def get_neighbors(pos):
    x, y = pos
    neighbors = []
    if x > 0:  # Left
        neighbors.append((x - 1, y))
    if x < 63:  # Right
        neighbors.append((x + 1, y))
    if y > 0:  # Up
        neighbors.append((x, y - 1))
    if y < 47:  # Down
        neighbors.append((x, y + 1))
    return neighbors

# Function to reconstruct and paint the BFS path
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # Optional: Include the start in the path
    path.reverse()  # Reverse the path to go from start to goal
    return path

# Starts pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Makes the key_state a start value which is grass
key_state = 0

# Makes running true, for the while loop
running = True

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
                # Perform BFS when spacebar is pressed
                frontier = Queue()
                start = (0, 0)  # Starting point of BFS
                goal = (63, 47)  # The goal to reach in the grid
                frontier.put(start)
                came_from = dict()  # path A->B is stored as came_from[B] == A
                came_from[start] = None

                while not frontier.empty():
                    current = frontier.get()

                    # Stop BFS when we reach the goal
                    if current == goal:
                        break

                    # Get the neighbors of the current node
                    for next in get_neighbors(current):
                        # Ensure the neighbor is not visited yet and not a water tile (assuming 1 is water)
                        if next not in came_from and grid[next[1]][next[0]] != 1:
                            frontier.put(next)
                            came_from[next] = current  # Mark the path

                # Reconstruct and draw the path
                path = reconstruct_path(came_from, start, goal)
                for step in path:
                    grid[step[1]][step[0]] = 'path'

                print("BFS completed. Path found:")
                for node in came_from:
                    print(f"Node {node} came from {came_from[node]}")

        # This detects the left mouse click [0]
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()  # Gets the mouse position (x, y)
            col = pos[0] // cell_size  # Divided by cell_size
            row = pos[1] // cell_size  # Divided by cell_size

            # Updates the grid value at the clicked position based on key_state
            grid[row][col] = key_state

            # ONLY FOR DEV, shares the values, what col, row and what value they have. This depends on the key_state
            print(f"Mouse clicked at grid position: (col={col}, row={row}) - Grid value changed to {key_state}")

    # Draws the grid
    for col in range(64):
        for row in range(48):
            color = colors.get(grid[row][col], (255, 0, 0))  # Default to red if no color found
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    pygame.display.flip()

pygame.quit()
