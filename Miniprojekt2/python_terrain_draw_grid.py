import pygame, sys
from main import handle_event_exit

grid_64x48 = [[0 for col in range(64)] for row in range(48)]

grid = grid_64x48
block_size = 10


keys = pygame.key.get_pressed
pygame.mouse.get_pressed

#Starter pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

running = True

pos = []
key_state = 0

while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


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


        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            x_ranges = [(i,i+10) for i in range(0, 640, 10)]
            y_ranges = [(i,i+10) for i in range(0, 480, 10)]

            for x_start, x_end in x_ranges:
                if x_start <= pos[0] < x_end:
                    for y_start, y_end in y_ranges:
                        if y_start <= pos[1] < y_end:
                            if key_state == 0:
                                print(f"The position is in the area: x between {x_start} and {x_end}, y between {y_start} and {y_end} and is activated with key 0")
                            elif key_state == 1:
                                print(f"The position is in the area: x between {x_start} and {x_end}, y between {y_start} and {y_end} and is activated with key 1")
                            elif key_state == 2:
                                print(f"The position is in the area: x between {x_start} and {x_end}, y between {y_start} and {y_end} and is activated with key 2")

            


    pygame.display.flip()

 

pygame.quit()