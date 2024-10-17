import pygame, sys

grid_64x48 = [[0 for col in range(64)] for row in range(48)]  # Grid size of 64x48

grid = grid_64x48
block_size = 10

# Function to draw the grid based on the terrain values
def draw_grid(screen, grid, block_size):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            terrain_type = grid[y][x]
            
            # Assign colors based on terrain type
            if terrain_type == 0:
                color = (0, 255, 0)  # Green for grass
            elif terrain_type == 1:
                color = (0, 0, 255)  # Blue for water
            elif terrain_type == 2:
                color = (128, 128, 128)  # Gray for mountains

            # Draw the block
            pygame.draw.rect(screen, color, pygame.Rect(x * block_size, y * block_size, block_size, block_size))

# Starter pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

running = True

key_state = 0

while running:
    screen.fill((255,255,255))  # White background

    # Draw the grid before handling events
    draw_grid(screen, grid, block_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                key_state = 0
                print("Key 0 has been pressed, and its special ability has been activated")

            if event.key == pygame.K_1:
                key_state = 1
                print("Key 1 has been pressed, and its special ability has been activated")

            if event.key == pygame.K_2:
                key_state = 2
                print("Key 2 has been pressed, and its special ability has been activated")

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # Get the mouse click position
            x = pos[0] // block_size  # Convert pixel position to grid position
            y = pos[1] // block_size

            if 0 <= x < 64 and 0 <= y < 48:  # Ensure we're inside the grid
                grid[y][x] = key_state  # Set the grid value to the key state (0, 1, or 2)
                print(f"Position ({x}, {y}) updated with key {key_state}")

    pygame.display.flip()  # Update the screen

pygame.quit()
