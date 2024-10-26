import pygame
import sys
from queue import Queue
from main import create_grid_64x48
from main import add_neighbors


#Laver grid 64x48
grid = create_grid_64x48()
cell_size = 10
start = (1,1)
goal = (62,46)

class Terrain_Types:
    def __init__(self, color, grid_number):
        self.color = color
        self.grid_number = grid_number

grass = Terrain_Types((30, 200, 30), 0)
wall = Terrain_Types((0, 0, 0), 1)

# Definerer en funktion til at finde gyldige naboer
add_neighbors(current)




#Opretter en kø kaldet frontier til at holde styr på de noder, der skal udforskes næste gang. I BFS bruges en kø for at sikre, at noderne udforskes i den rækkefølge, de tilføjes.
frontier = Queue()
#Tilføjer start-noden (startpunktet for søgningen) til frontier-køen. Dette markerer noden som den første, der skal udforskes.
frontier.put(start)
#Initialiserer en tom ordbog (dictionary) kaldet came_from, som vil gemme stien fra hver node. 
#For hver node B vil came_from[B] angive den node A, der førte til B, hvilket gør det muligt at spore tilbage og genskabe stien, når målet er nået.
came_from = dict()
#Sætter start-nodens forgænger til None, da den ikke har nogen forudgående node i stien. 
#Dette hjælper senere, når man genskaber stien fra startnoden.
came_from[start] = None
#Starter en løkke, der fortsætter, så længe der er noder i frontier-køen, hvilket betyder, at der stadig er noder tilbage at udforske.
while not frontier.empty():
#Fjerner og henter den næste node, der skal udforskes fra frontier-køen, og gemmer den i current
    current = frontier.get()
#Går igennem alle nabonoder (next) til current-noden. 
#Her undersøges hver nabo for at se, om den allerede er blevet udforsket.
    for next in add_neighbors(current):
#Tjekker, om next-noden ikke er blevet besøgt før (dvs., den er ikke i came_from-ordbogen). 
#Hvis next allerede er besøgt, springes den over for at undgå at udforske noder igen.
        if next not in came_from:
#Tilføjer den uudforskede nabonode (next) til frontier-køen, så den vil blive udforsket i fremtidige gentagelser.
            frontier.put(next)
#Registrerer, at det er current, der førte til next, ved at sætte came_from[next] = current. 
#Dette hjælper med at spore stien tilbage fra enhver node til startnoden senere.
            came_from[next] = current



#Sætter current til slutnoden (goal), da vi starter med at gå baglæns fra målet for at finde hele vejen tilbage til startnoden.
current = goal
#Opretter en tom liste kaldet path, som skal gemme rækkefølgen af noder fra start til mål.
path = []
#Starter en løkke, som fortsætter, indtil vi når startnoden. På hvert trin bevæger vi os baglæns langs stien, der blev gemt i came_from.
while current != start:
#Tilføjer current (den nuværende node) til path. Dette bygger stien op bagfra, fra goal til start.
    path.append(current)
#Opdaterer current til noden, der førte til den nuværende node, ved at slå op i came_from. Dette bevæger os ét skridt længere mod startnoden.
    current = came_from[current]
#Tilføjer start til path, når løkken er færdig. Dette er valgfrit, da startnoden allerede kan være implicit forstået som begyndelsen af stien.
path.append(start)
#Vender path-listen om, så rækkefølgen bliver fra start til goal i stedet for omvendt. Dette er også valgfrit, afhængigt af hvordan man vil præsentere stien.
path.reverse()


#Starts pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))


#Makes running true, for the while loop
running = True

while running:
    screen.fill((255,255,255)) #This is not important

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for col in range(64):
        for row in range(48):
            if grid[col][row] == grass.grid_number:
                pygame.draw.rect(screen, grass.color, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif grid[col][row] == wall.grid_number:
                pygame.draw.rect(screen, wall.color, (col * cell_size, row * cell_size, cell_size, cell_size))
    
     # Tegn sti
    for pos in path:
        pygame.draw.rect(screen, (255, 0, 0), (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
    
    pygame.display.flip()



pygame.quit()