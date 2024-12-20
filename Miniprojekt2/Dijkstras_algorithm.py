import pygame
from queue import PriorityQueue
from main import Terrain_Types


#Starts pygame
pygame.init()
screen = pygame.display.set_mode((930, 480))

#Laver grid 64x48 med default værdi for grass
grid_64x48 = [[3 for row in range(48)] for col in range(64)]
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
grass = Terrain_Types((30, 200, 30), 3)
desert = Terrain_Types((210, 180, 120), 5)
mountain = Terrain_Types((105,105,105), 7)
water = Terrain_Types((0, 105, 148), 6)
forest = Terrain_Types((25, 80, 25), 4)
road = Terrain_Types((50, 50, 50), 2) 
wall = Terrain_Types((0, 0, 0), 10000)#Not passable (Trumps wall to Mexican border)

#Liste med alle grid numre, så de kan loopes igennem
valid_key_states = [grass.grid_number, desert.grid_number, mountain.grid_number, water.grid_number, forest.grid_number, road.grid_number, wall.grid_number]


#Starter med at lave gras (Fejlsikring som defualt setting, da det ellers vil lukke ned, hvis man trykker på skærmen)
key_state = grass.grid_number


def neighbors(current):
    """Funktionen her sørger for at finde alle naboer til en cell"""
    x, y = current
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #Op, højre, ned, venstre
    neighbors = []
    for dx, dy in directions: 
        nx, ny = x + dx, y + dy
        if 0 <= nx < 64 and 0 <= ny < 48:  #Sørger for at være indenfor grænserne
            neighbors.append((nx, ny))
    return neighbors

def cost(current, next):
    """Definere hvad cost der skal være, ved de forskellige celler"""
    x, y = next
    if grid_64x48[x][y] == grass.grid_number:
        return grass.grid_number
    elif grid_64x48[x][y] == desert.grid_number:
        return desert.grid_number
    elif grid_64x48[x][y] == mountain.grid_number:
        return mountain.grid_number
    elif grid_64x48[x][y] == water.grid_number:
        return water.grid_number
    elif grid_64x48[x][y] == forest.grid_number:
        return forest.grid_number
    elif grid_64x48[x][y] == road.grid_number:
        return road.grid_number
    elif grid_64x48[x][y] == wall.grid_number:
        return wall.grid_number

def dijkstra(grid_64x48, start, goal):
    """Funktionen her implementerer dijkstra for at finde den koreste sti fra start til mål"""
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break
    
        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current


    return came_from


def reconstruct_path(came_from, start, goal):
    """Funktionen her sørger for at reconstruere stien fra start til goal"""
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  #Tilføj start til slutningen
    path.reverse()  #Reverserer listen for at få stien fra start til mål
    return path






#Makes running true, for the while loop
running = True
path = []

while running:
    screen.fill((160, 160, 160))  #Ændrer egentlig kun farven på højre side

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Registrer alle muligheder for at trykke forskellige taster på keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key_state = grass.grid_number
            elif event.key == pygame.K_2:
                key_state = desert.grid_number
            elif event.key == pygame.K_3:
                key_state = mountain.grid_number
            elif event.key == pygame.K_4:
                key_state = water.grid_number
            elif event.key == pygame.K_5:
                key_state = forest.grid_number
            elif event.key == pygame.K_6:
                key_state = road.grid_number
            elif event.key == pygame.K_0:
                key_state = wall.grid_number
            elif event.key == pygame.K_SPACE:
                came_from = dijkstra(grid_64x48, start, goal)  #Start path finding, når space presses
                path = reconstruct_path(came_from, start, goal)
                print("Pathfinding algorithm activated")
            elif event.key == pygame.K_g:
                key_state = "goal"
            elif event.key == pygame.K_s:
                key_state = "start"
            elif event.key == pygame.K_r:
                path.clear()
            elif event.key == pygame.K_t:
                grid_64x48.clear()
                grid_64x48 = [[3 for row in range(48)] for col in range(64)]
        

            

    #Registrer om venstre musseklik presses
    if pygame.mouse.get_pressed()[0]:
        if key_state in valid_key_states: #Kontrollere alle valid key states
            pos = pygame.mouse.get_pos()
            if pos[0] >= 0 and pos[0] <= 63 * cell_size and pos[1] >= 0 and pos[1] <= 47 * cell_size:
                col = pos[0] // cell_size
                row = pos[1] // cell_size
                grid_64x48[col][row] = key_state
        elif key_state == "goal":
            pos = pygame.mouse.get_pos()
            if pos[0] >= 0 and pos[0] <= 63 * cell_size and pos[1] >= 0 and pos[1] <= 47 * cell_size:
                goal_list[0] = pos[0] // cell_size
                goal_list[1] = pos[1] // cell_size
                goal = tuple(goal_list)
        elif key_state == "start":
            pos = pygame.mouse.get_pos()
            if pos[0] >= 0 and pos[0] <= 63 * cell_size and pos[1] >= 0 and pos[1] <= 47 * cell_size:
                start_list[0] = pos[0] // cell_size
                start_list[1] = pos[1] // cell_size
                start = tuple(start_list)
            

            



    #Tegner grid alle valid_key_states
    for col in range(64):
        for row in range(48):
            if grid_64x48[col][row] == grass.grid_number:
                pygame.draw.rect(screen, grass.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid_64x48[col][row] == desert.grid_number:
                pygame.draw.rect(screen, desert.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid_64x48[col][row] == mountain.grid_number:
                pygame.draw.rect(screen, mountain.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid_64x48[col][row] == water.grid_number:
                pygame.draw.rect(screen, water.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid_64x48[col][row] == forest.grid_number:
                pygame.draw.rect(screen, forest.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid_64x48[col][row] == road.grid_number:
                pygame.draw.rect(screen, road.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid_64x48[col][row] == wall.grid_number:
                pygame.draw.rect(screen, wall.color, (col * cell_size, row * cell_size, cell_size, cell_size))
    
    

    #Tegn sti
    for pos in path:
        pygame.draw.rect(screen, (150, 25, 200), (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))

    pygame.draw.rect(screen, (200, 30, 30), (start_list[0] * cell_size, start_list[1] * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, (30, 30, 200), (goal_list[0] * cell_size, goal_list[1] * cell_size, cell_size, cell_size))


    #Opdater tekstfarve baseret på key_state
    if key_state == grass.grid_number:
        text_grass = font.render("1 to change grass", True, green)
    else:
        text_grass = font.render("1 to change grass", True, red)
    
    if key_state == desert.grid_number:
        text_desert = font.render("2 to change desert", True, green)
    else:
        text_desert = font.render("2 to change desert", True, red)

    if key_state == mountain.grid_number:
        text_mountain = font.render("3 to change mountain", True, green)
    else:
        text_mountain = font.render("3 to change mountain", True, red)

    if key_state == water.grid_number:
        text_water = font.render("4 to change water", True, green)
    else:
        text_water = font.render("4 to change water", True, red)

    if key_state == forest.grid_number:
        text_forest = font.render("5 to change forest", True, green)
    else:
        text_forest = font.render("5 to change forest", True, red)

    if key_state == road.grid_number:
        text_road = font.render("6 to change road", True, green)
    else:
        text_road = font.render("6 to change road", True, red)

    if key_state == wall.grid_number:
        text_wall = font.render("0 to change wall", True, green)
    else:
        text_wall = font.render("0 to change wall", True, red)

    if key_state == "start":
        text_start = font.render("s to change start", True, green)
    else:
        text_start = font.render("s to change start", True, red)

    if key_state == "goal":
        text_goal = font.render("g to change goal", True, green)
    else:
        text_goal = font.render("g to change goal", True, red)

    text_path = font.render("Space to find path", True, (0,0,0))
    reset_path = font.render("r to reset path", True, (0,0,0))
    reset_terrain = font.render("t to reset terrain", True, (0,0,0))

    #Position af text
    text_rect_grass = text_grass.get_rect(center=(750,20))
    text_rect_dessert = text_desert.get_rect(center=(755,50))
    text_rect_mountain = text_mountain.get_rect(center=(774,80))
    text_rect_water = text_water.get_rect(center=(750,110))
    text_rect_forest = text_forest.get_rect(center=(752,140))
    text_rect_road = text_road.get_rect(center=(745,170))
    text_rect_wall = text_wall.get_rect(center=(742,200))
    text_rect_start = text_start.get_rect(center=(745,230))
    text_rect_goal = text_goal.get_rect(center=(745,260))
    text_rect_path = text_path.get_rect(center=(750,290))
    text_rect_reset_path = reset_path.get_rect(center=(725, 320))
    text_rect_reset_terrain = reset_terrain.get_rect(center=(737, 350))

    #Visning af text
    screen.blit(text_grass, text_rect_grass)
    screen.blit(text_desert, text_rect_dessert)
    screen.blit(text_mountain, text_rect_mountain)
    screen.blit(text_water, text_rect_water)
    screen.blit(text_forest, text_rect_forest)
    screen.blit(text_road, text_rect_road)
    screen.blit(text_wall, text_rect_wall)
    screen.blit(text_start, text_rect_start)
    screen.blit(text_goal, text_rect_goal)
    screen.blit(text_path, text_rect_path)
    screen.blit(reset_path, text_rect_reset_path)
    screen.blit(reset_terrain, text_rect_reset_terrain)


    pygame.display.flip()

pygame.quit()
