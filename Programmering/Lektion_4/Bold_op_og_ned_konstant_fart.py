import pygame
import math
import pygame.time



pygame.init()
screen = pygame.display.set_mode((840, 640))

clock=pygame.time.Clock()
fps=300 #farten af cirklen kan defineres ved at ændre fps

while True:
    
    
    start_x=420
    start_y=320
    for fremad in range(-200,201):#Kører alle værdier fra -200 til 201
        screen.fill((255,255,255)) #Fylder hele tiden skærmen bagved med hvid farve
        pygame.draw.circle(screen, (0,0,0),(start_x,start_y+fremad),20) #Her laver vi cirklen og ændrer cirklen på y-aksen
        pygame.display.flip()
        clock.tick(fps)
        

    for tilbage in range(200,-201,-1):#Starter på 200 og får -1 indtil -201
        screen.fill((255,255,255))
        pygame.draw.circle(screen, (0,0,0),(start_x,start_y+tilbage),20) #Her laver vi cirklen og ændrer cirklen på y-aksen
        pygame.display.flip()
        clock.tick(fps) #Ændrer clock tick for at ændre cirklens fart. 





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()