import pygame,sys

def start_pygame(screen_size):
    """Start Pygame og sætter op en skærm"""
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    return screen

def handle_event_exit():
    """Handler for events som at lukke spillet"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False  # Returnér False for at stoppe spillet
    return True  # Fortsæt spillet ellers


def update_screen(screen, color):
    """Opdatere skærmen"""
    screen.fill(color)
    pygame.display.flip()


def create_grid_64x48():
    """Laver en liste med 64x48 0'er"""
    global grid_64x48
    grid_64x48 = [[0 for row in range(48)] for col in range(64)]
    return grid_64x48



class Terrain_Types:
    """Laver klasserne med grass og væg"""
    def __init__(self, color, grid_number):
        self.color = color
        self.grid_number = grid_number





def add_neighbors(current):
    """Definerer en funktion til at finde gyldige naboer"""
    neighbors = []
    x, y = current
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #Op, højre, ned, venstre

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 64 and 0 <= ny < 48:  #Sørger for at være indenfor grænserne
            if grid_64x48[nx][ny] == 0:  #Tjekker om cellen er græs altså = 0
                neighbors.append((nx, ny))
    return neighbors




def find_path(start,goal):
    """Funktionen her implementerer BFS for at finde den koreste sti fra start til mål"""
    from queue import Queue
    frontier = Queue() #Starter køen, som bruges til at holde styr på cellerne, som der skal udforskes
    frontier.put(start) #Tilføjer startpunktet til køen
    came_from = dict() #Tilføjer en dictionary, som skal bruges til at holde styr på cellerne, så vi kan spores stien tilbage
    came_from[start] = None  #Her er vores startpunkt

    while not frontier.empty(): #While loop, så der udforskes celler, så længe der er celler der kan udforskes
        current = frontier.get() #Fjerner den næste celle fra køen

        if current == goal: #Stopper algoritmen, når målet er nået. 
            break

        for next in add_neighbors(current): #Kikker alle naboer til current celle igennem (Bruger add_neighbors funktionen)
            if next not in came_from: #Kontrollere om den har været ved den før
                frontier.put(next) #Tilføjer naboen til køen
                came_from[next] = current #Ser om naboen blev udforsket fra den nuværende celle

    #Genskaber stien fra goal til start
    current = goal #Starter fra målet for at finde stien tilbage til start.
    path = [] #Laver en liste, som stien kan gemmes i.
    if current in came_from: 
        while current != start: #Følger stien tilbage fra mål til start.
            path.append(current) #Tilføjer cellen til stien.
            current = came_from[current] #Går til forældrecellen.
        path.append(start) #Tilføjer startcellen til stien.
        path.reverse() #Vender stien om, så den går fra start til mål.

    return path


def draw_horizontal(grid_64x48, row, start_col, end_col):
    """Vandret, ændrer fx række 10, fra kolonne 5 til 15"""
    for col in range(start_col, end_col + 1): #Plus 1 skyldes at det vil give det rigtige antal, så man ikke skal tænke på at sætte ekstra ind
        grid_64x48[row][col] = 1  # Sætter 1-taller fra kolonne 5 til 15 i række 10




def draw_vertical(grid, col, start_row, end_row):
    """Lodret, ændrer fx kolonne 20 fra række 5 til 15"""
    for row in range(start_row, end_row + 1): #Plus 1 skyldes at det vil give det rigtige antal, så man ikke skal tænke på at sætte ekstra ind
        grid_64x48[row][col] = 1  # Sætter 1-taller fra række 5 til 15 i kolonne 20