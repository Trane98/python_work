import pygame, sys
from main import handle_event_exit
from queue import Queue

#Makes the grid 64x48
grid = [[0 for col in range(64)] for row in range(48)]


#The size for the pixels
cell_size = 10

#Colors
colors = {0: (30, 200, 30), #Green
          1: (30, 30 ,200), #Blue
          2: (125, 125, 125), #Grey
          "path": (255, 255, 0) #Yellow
          }





#Starts pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

#Makes the key_state a start value which is grass
key_state = 0

#Makes running true, for the while loop
running = True

while running:
    screen.fill((255,255,255)) #This is not important

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        #Registers the key which is pressed, activates the key, which makes the terrain different
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
                    #perform BFS when space is pressed


        #This detects the left mouse click [0]
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos() #Gets the mouse position (x, y)
            col = pos[0] // cell_size #Divided by cell_size
            row = pos[1] // cell_size #Divided by cell_size

            #Updates the grid value, at the clicked position based on key_state
            grid[row][col] = key_state

            #ONLY FOR DEV, shares the values, what col, row and what value they have. This depends on the key_state
            print(f"Mouse clicked at grid position: (col={col}, row={row}) - Grid value changed to {key_state}")
    #Draws the grid
    for col in range(64):
        for row in range(48):
            color = colors[grid[row][col]]
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

        


            


    pygame.display.flip()

 

pygame.quit()