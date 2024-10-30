import pygame
from main import Terrain_Types
from main import create_grid_64x48
from main import add_neighbors
from main import find_path
from main import draw_horizontal
from main import draw_vertical

#Laver grid 64x48 og laver cell size
grid_64x48 = create_grid_64x48()
cell_size = 10

draw_horizontal(grid_64x48, 1, 1, 1)
draw_vertical(grid_64x48, 1, 1, 1)


#Klasserne og deres tilhørende værdier (Farve og tilhørende grid-nummer)
grass = Terrain_Types((30, 200, 30), 0)
wall = Terrain_Types((0, 0, 0), 1)



#Starter med at lave gras (Fejlsikring som defualt setting, da det ellers vil lukke ned, hvis man trykker på skærmen)
key_state = grass.grid_number

#Starts pygame
pygame.init()
screen = pygame.display.set_mode((840, 480))

#Makes running true, for the while loop
running = True
path = []

while running:
    screen.fill((255, 255, 255))  #Kan egentlig bare slettes til sidst

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Registrer 0,1 og space, til at ændre i grid eller starte algorithmen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                key_state = grass.grid_number
                print("Key 0 has been pressed, and its special ability has been activated")
            elif event.key == pygame.K_1:
                key_state = wall.grid_number
                print("Key 1 has been pressed, and its special ability has been activated")
            elif event.key == pygame.K_SPACE:
                path = find_path((1,1),(62,46))  #Find path when spacebar is pressed
                print("Pathfinding algorithm activated")

    #Registrer om venstre musseklik presses
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        col = pos[0] // cell_size
        row = pos[1] // cell_size
        grid_64x48[col][row] = key_state

    #Tegner grid "0" og "1"
    for col in range(64):
        for row in range(48):
            if grid_64x48[col][row] == grass.grid_number:
                pygame.draw.rect(screen, grass.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid_64x48[col][row] == wall.grid_number:
                pygame.draw.rect(screen, wall.color, (col * cell_size, row * cell_size, cell_size, cell_size))

    #Tegn sti
    for pos in path:
        pygame.draw.rect(screen, (255, 0, 0), (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))

    pygame.display.flip()

pygame.quit()
