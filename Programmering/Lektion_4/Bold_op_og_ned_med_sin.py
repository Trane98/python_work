import pygame
import math
import pygame.time



pygame.init()
screen = pygame.display.set_mode((840, 640))

clock=pygame.time.Clock()

while True:
    start_x=420
    start_y=320
    for i in range(0,361):# for at sætte de 360 grader
        angle = math.radians(i) #Omregne fra grader til radianer
        screen.fill((255,255,255)) #Fylder hele tiden skærmen bagved med hvid farve
        pygame.draw.circle(screen, (0,0,0),(start_x,start_y+math.sin(angle)*300),20) #Her laver vi cirklen og ændrer cirklen på y-aksen
        pygame.display.flip()
        clock.tick(60) #Ændrer clock tick for at ændre cirklens fart. 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()