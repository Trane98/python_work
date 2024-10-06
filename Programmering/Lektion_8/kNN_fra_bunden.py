import random
import pygame
from main import handle_event_exit

SALMON_COLOR = (255, 102, 102)
BASS_COLOR = (50,255, 50)
UNKNOWN = (0,0,0)

#Make a class to contain a data point. The class must be able to contain an x-y-position of the data point, a class label, and a color.
class DataPoint:
    def __init__(self, x,y, label, color):
        self.x = x
        self.y = y
        self.label = label
        self.color = color

data_points = []
for _ in range(10):
    x = random.gauss(200,20)
    y = random.gauss(200,20)
    data_points.append(DataPoint(x,y, "salmon", SALMON_COLOR))

for _ in range(10):
    x = random.gauss(400, 20)
    y = random.gauss(200,20)
    data_points.append(DataPoint(x,y, "bass", BASS_COLOR))

data_points.append(DataPoint(240,150, "UNKNOWN", UNKNOWN))

#Starter pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))


running = True

while running:
    screen.fill((255,255,255))

    for data_point in data_points:
        pygame.draw.circle(screen, data_point.color, (int(data_point.x), int(data_point.y)), 5)



    pygame.display.flip()

    running = handle_event_exit()

pygame.quit()