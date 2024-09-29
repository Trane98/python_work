import pygame , sys
from datetime import datetime
import math
import pygame.key
import random
from math import sqrt

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
 
# initialize pygame
pygame.init()
screen_size = (840, 680)
 
# create a window
screen = pygame.display.set_mode(screen_size)
 
# clock is used to set a max fps
clock = pygame.time.Clock()

#Rect informations (starting point and box_size)
box_position = [370, 290]
box_size = [20, 20]

#Variabler til bevægelse
x = 0
y = 0

#Changes the speed of the rect
max_speed = 5

#This part generates a list of 10 guldklumper, where their position is random generated. 

guldklump0 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump1 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump2 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump3 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump4 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump5 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump6 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump7 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump8 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}
guldklump9 = {"color" : YELLOW, "radius" : 10, "position" : (random.uniform(0,840), random.uniform(0,680)),}


x0, y0 = guldklump0["position"]
x1, y1 = guldklump1["position"]
x2, y2 = guldklump2["position"]
x3, y3 = guldklump3["position"]
x4, y4 = guldklump4["position"]
x5, y5 = guldklump5["position"]
x6, y6 = guldklump6["position"]
x7, y7 = guldklump7["position"]
x8, y8 = guldklump8["position"]
x9, y9 = guldklump9["position"]




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()
    
    #Changing the movements of which and how keys are pressed
    if keys[pygame.K_a]:
        x -= 5
    if keys[pygame.K_d]:
        x += 5
    if keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_s]:
        y += 5
    if keys[pygame.K_SPACE]: #Space makes the rect go still
        x = 0 
        y = 0


    #Makes a max speed, so it will never exceed the max_speed value for x and y
    if x > max_speed:
        x = max_speed
    elif x < -max_speed:
        x = -max_speed

    if y > max_speed:
        y = max_speed
    elif y < -max_speed:
        y = -max_speed



    #Opdates the box's position by adding the x and y value pressed
    box_position[0] += x
    box_position[1] += y

    #Ændrer rect position, hvis den går ud over kanterne
    if box_position[0] > 840:
        box_position[0] = -20

    if box_position[0] < -20:
        box_position[0] = 840

    if box_position[1] > 680:
        box_position[1] = -20

    if box_position[1] < -20:
        box_position[1] = 680


    #clear the screen
    screen.fill(WHITE)

    

    #Make rectangle
    pygame.draw.rect(screen, (BLACK), (box_position[0], box_position[1], box_size[0], box_size[1]))



    distance0 = sqrt((box_position[0]-x0)**2+(box_position[1]-y0)**2)
    distance1 = sqrt((box_position[0]-x1)**2+(box_position[1]-y1)**2)
    distance2 = sqrt((box_position[0]-x2)**2+(box_position[1]-y2)**2)
    distance3 = sqrt((box_position[0]-x3)**2+(box_position[1]-y3)**2)
    distance4 = sqrt((box_position[0]-x4)**2+(box_position[1]-y4)**2)
    distance5 = sqrt((box_position[0]-x5)**2+(box_position[1]-y5)**2)
    distance6 = sqrt((box_position[0]-x6)**2+(box_position[1]-y6)**2)
    distance7 = sqrt((box_position[0]-x7)**2+(box_position[1]-y7)**2)
    distance8 = sqrt((box_position[0]-x8)**2+(box_position[1]-y8)**2)
    distance9 = sqrt((box_position[0]-x9)**2+(box_position[1]-y9)**2)
    

    #Goes though the guldklumper_list and generates the circles from the list.
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump0["color"], guldklump0["position"], guldklump0["radius"])    
    if distance0 > 15:    
        pygame.draw.circle(screen, guldklump1["color"], guldklump1["position"], guldklump1["radius"])
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump2["color"], guldklump2["position"], guldklump2["radius"])
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump3["color"], guldklump3["position"], guldklump3["radius"])
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump4["color"], guldklump4["position"], guldklump4["radius"])
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump5["color"], guldklump5["position"], guldklump5["radius"])
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump6["color"], guldklump6["position"], guldklump6["radius"])
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump7["color"], guldklump7["position"], guldklump7["radius"])
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump8["color"], guldklump8["position"], guldklump8["radius"])
    if distance0 > 15:
        pygame.draw.circle(screen, guldklump9["color"], guldklump9["position"], guldklump9["radius"])
    

    
    pygame.display.flip()





    # how many updates per second
    clock.tick(60)


pygame.quit()