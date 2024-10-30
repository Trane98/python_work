import pygame
import sys
from queue import Queue

#Laver grid 64x48
grid_64x48 = [[0 for row in range(48)] for col in range(64)]
cell_size = 10
start = (1, 1)
goal = (62, 46)
key_state = 0

class Terrain_Types:
    def __init__(self, color, grid_number):
        self.color = color
        self.grid_number = grid_number

grass = Terrain_Types((30, 200, 30), 0)
wall = Terrain_Types((0, 0, 0), 1)

#Definerer en funktion til at finde gyldige naboer
def add_neighbors(current):
    neighbors = []
    x, y = current
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #Op, højre, ned, venstre

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 64 and 0 <= ny < 48:  #Sørger for at være indenfor grænserne
            if grid_64x48[nx][ny] == grass.grid_number:  #Tjekker om cellen er græs altså = 0
                neighbors.append((nx, ny))
    return neighbors

#Funktion til at finde stien
"""Funktionen her implementerer BFS for at finde den koreste sti fra start til mål"""
def find_path():
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

#Starts pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

#Makes running true, for the while loop
running = True
path = []

while running:
    screen.fill((255, 255, 255))  #This is not important

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Registrer 0,1 og space, til at ændre i grid eller starte algorithmen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                key_state = 0
                print("Key 0 has been pressed, and its special ability has been activated")
            elif event.key == pygame.K_1:
                key_state = 1
                print("Key 1 has been pressed, and its special ability has been activated")
            elif event.key == pygame.K_SPACE:
                path = find_path()  #Find path when spacebar is pressed
                print("Pathfinding algorithm activated")

    #Detects left mouse click to change terrain
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
