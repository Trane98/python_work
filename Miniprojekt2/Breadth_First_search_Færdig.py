import pygame, sys
from main import Terrain_Types
from main import create_grid_64x48
from main import add_neighbors
from main import find_path
from main import draw_horizontal
from main import draw_vertical

#Starts pygame
pygame.init()
screen = pygame.display.set_mode((880, 480))

#Laver grid 64x48 og laver cell size
grid_64x48 = create_grid_64x48()
#Til at få pixel og grid overens
cell_size = 10

#Laver start og slut (2 laves grundet agoritme og liste ikke fungere)
start_list = [1, 1]
start = (1,1)
goal_list = [62, 46]
goal = (62,46)

#Farver til text
green = (30,200,30)
red = (200, 30, 30)

#Font setup
font = pygame.font.Font(None, 36) #None giver en defualt font, og tallet efter, er font size. 


#Klasserne og deres tilhørende værdier (Farve og tilhørende grid-nummer)
grass = Terrain_Types((30, 200, 30), 0)
wall = Terrain_Types((0, 0, 0), 1)


#Starter med at lave gras (Fejlsikring som defualt setting, da det ellers vil lukke ned, hvis man trykker på skærmen)
key_state = grass.grid_number


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
            elif event.key == pygame.K_1:
                key_state = wall.grid_number
            elif event.key == pygame.K_SPACE:
                path = find_path(start,goal)  #Start path finding, når space presses
                print("Pathfinding algorithm activated")
            elif event.key == pygame.K_g:
                key_state = "goal"
            elif event.key == pygame.K_s:
                key_state = "start"
        

            

    #Registrer om venstre musseklik presses
    if pygame.mouse.get_pressed()[0]:
        if key_state == 0 or key_state == 1:
            pos = pygame.mouse.get_pos()
            col = pos[0] // cell_size
            row = pos[1] // cell_size
            grid_64x48[col][row] = key_state
        elif key_state == "goal":
            pos = pygame.mouse.get_pos()
            goal_list[0] = pos[0] // cell_size
            goal_list[1] = pos[1] // cell_size
            goal = tuple(goal_list)
        elif key_state == "start":
            pos = pygame.mouse.get_pos()
            start_list[0] = pos[0] // cell_size
            start_list[1] = pos[1] // cell_size
            start = tuple(start_list)
            

            

 


    #Tegner grid "0" og "1"
    for col in range(64):
        for row in range(48):
            if grid_64x48[col][row] == grass.grid_number:
                pygame.draw.rect(screen, grass.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid_64x48[col][row] == wall.grid_number:
                pygame.draw.rect(screen, wall.color, (col * cell_size, row * cell_size, cell_size, cell_size))
    
    

    #Tegn sti
    for pos in path:
        pygame.draw.rect(screen, (150, 25, 200), (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))

    pygame.draw.rect(screen, (200, 30, 30), (start_list[0] * cell_size, start_list[1] * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, (30, 30, 200), (goal_list[0] * cell_size, goal_list[1] * cell_size, cell_size, cell_size))

    #Laver ramme til mappet (Vil altid være dominerende så længe i while-loopet)
    draw_horizontal(grid_64x48, 0, 0, 63)
    draw_horizontal(grid_64x48, 47, 0, 63)
    draw_vertical(grid_64x48, 0, 0, 47)
    draw_vertical(grid_64x48, 63, 0, 47)


    #Render text (Default settings)
    text_grass = font.render("0 to change grass", True, (red)) #True aktiverer anti-aliasing
    text_wall = font.render("1 to change wall", True, (red))
    text_start = font.render("s to change start", True, (red))
    text_goal = font.render("g to change goal", True, (red))
    text_path = font.render("Space to find path", True, (0,0,0))


    #Position af text
    text_rect_grass = text_grass.get_rect(center=(750,20))
    text_rect_wall = text_wall.get_rect(center=(742,50))
    text_rect_start = text_grass.get_rect(center=(750,80))
    text_rect_goal = text_wall.get_rect(center=(742,110))
    text_rect_path = text_grass.get_rect(center=(748,140))

    #Opdater tekstfarve baseret på key_state
    if key_state == grass.grid_number:
        text_grass = font.render("0 to change grass", True, green)
    else:
        text_grass = font.render("0 to change grass", True, red)

    if key_state == wall.grid_number:
        text_wall = font.render("1 to change wall", True, green)
    else:
        text_wall = font.render("1 to change wall", True, red)

    if key_state == "start":
        text_start = font.render("s to change start", True, green)
    else:
        text_start = font.render("s to change start", True, red)

    if key_state == "goal":
        text_goal = font.render("g to change goal", True, green)
    else:
        text_goal = font.render("g to change goal", True, red)


    #Visning af text
    screen.blit(text_grass, text_rect_grass)
    screen.blit(text_wall, text_rect_wall)
    screen.blit(text_start, text_rect_start)
    screen.blit(text_goal, text_rect_goal)
    screen.blit(text_path, text_rect_path)


    pygame.display.flip()

pygame.quit()
