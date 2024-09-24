import pygame
import math
from datetime import datetime


pygame.init()
screen = pygame.display.set_mode((840, 640))

while True:
    screen.fill((255,255,255))
    x_start, y_start = 420, 340
    length = 250
    width = 4

    current_time = datetime.now().second #Sekunder siden sidste minut
    angle = math.radians((current_time / 60) * 360)  #Converterer tid til vinkel
    
    
    x_end = x_start + length * math.cos(angle)
    y_end = y_start + length * math.sin(angle)
    
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end), width)
    pygame.display.flip()

    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



clock.tick(60)