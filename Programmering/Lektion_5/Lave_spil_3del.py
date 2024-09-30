import pygame
from datetime import datetime
import math
import pygame.key
import random
from math import sqrt

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)

# initialize pygame
pygame.init()
screen_size = (840, 680)
screen = pygame.display.set_mode(screen_size)

# clock is used to set a max fps
clock = pygame.time.Clock()


# Rect information (starting point and box_size)
box_position = [370, 290]
box_size = [20, 20]

# Variables for movement for rect
x_box = 0
y_box = 0

# Changes the speed of the rect
max_speed = 5

#Points related individuel point and their total
guldklumper_points_individuel = []
total_points = []

#Text for total score and the goldnugget score
font_total_score = pygame.font.SysFont("Arial", 36)
font_nugget_points = pygame.font.SysFont("Arial", 15)


guldklumper = []
# Generate a list of 10 gold nuggets with random positions
for i in range(10):
    guldklumper.append({
        "color": YELLOW,
        "radius": 10,
        "position": (random.uniform(0, 840), random.uniform(0, 680)),
        "points": random.uniform(0,100)
    })

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    ####################################################### RECT CODE PART DOWN #########################################################

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # Changing the movements based on which keys are pressed
    if keys[pygame.K_a]:
        x_box -= 5
    if keys[pygame.K_d]:
        x_box += 5
    if keys[pygame.K_w]:
        y_box -= 5
    if keys[pygame.K_s]:
        y_box += 5
    if keys[pygame.K_SPACE]:  # Space makes the rect go still
        x_box = 0
        y_box = 0

    # Ensure the rect doesn't exceed max_speed
    x_box = max(-max_speed, min(x_box, max_speed))
    y_box = max(-max_speed, min(y_box, max_speed))

    # Update the box's position
    box_position[0] += x_box
    box_position[1] += y_box

    # Wrap the rect position if it goes off-screen
    if box_position[0] > 840:
        box_position[0] = -20
    if box_position[0] < -20:
        box_position[0] = 840
    if box_position[1] > 680:
        box_position[1] = -20
    if box_position[1] < -20:
        box_position[1] = 680

    # Make rectangle
    pygame.draw.rect(screen, BLACK, (box_position[0] - box_size[0] / 2, box_position[1] - box_size[1] / 2, box_size[0], box_size[1]))

    ####################################################### RECT CODE PART ABOVE #########################################################

    ####################################################### GULDKLUMPER BELOW #########################################################

    # Draw the gold nuggets and the text for ther actual points
    for guldklump in guldklumper:
        pygame.draw.circle(screen, YELLOW, guldklump["position"], guldklump["radius"] + guldklump["points"])
        text_goldnugget_individual_points = str(int(guldklump["points"]))
        text_surface_nuggets = font_nugget_points.render(text_goldnugget_individual_points, True, BLACK)
        text_rect = text_surface_nuggets.get_rect(center=guldklump["position"])
        # Tegn teksten på skærmen centreret over guldklumpen
        screen.blit(text_surface_nuggets, text_rect)
    

    # Collision detection with pythagoras and gold nugget removal
    for guldklump in guldklumper[:]:
        distance = math.sqrt((box_position[0] - guldklump["position"][0])**2 + (box_position[1] - guldklump["position"][1])**2)
        if distance < guldklump["radius"] + guldklump["points"]:
            guldklumper_points_individuel.append (guldklump["points"])
            guldklumper.remove(guldklump)

    ####################################################### GULDKLUMPER ABOVE #########################################################

    ####################################################### POINT SYSTEM BELOW #########################################################

    #Adds the lists points together
    total_points = sum(guldklumper_points_individuel)

    #Point system left corner of the screen
    text_current_score = f"Your score is: {int(total_points)}"
    text_surface = font_total_score.render(text_current_score, True, BLACK)  # Sort tekst
    screen.blit(text_surface, (10, 10))  # Tegn teksten på skærmen

    ####################################################### POINT SYSTEM ABOVE #########################################################

    pygame.display.flip()

    # How many updates per second
    clock.tick(30)

pygame.quit()
