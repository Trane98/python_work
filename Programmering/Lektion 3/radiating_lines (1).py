import pygame
import math

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
screen.fill((255, 255, 255))

start_position = (screen_size[0]/2, screen_size[1]/2)

radius = 200
for angle in range(0, 360, 30):
    end_offset = [radius*math.cos(math.radians(angle)), radius*math.sin(math.radians(angle))]
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
    pygame.draw.line(screen, (0,0,0), start_position, end_position, 5)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()