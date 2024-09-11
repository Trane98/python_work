import pygame
from math import sin, cos, radians
from datetime import datetime

# Initialize pygame and clock
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

def draw_hand(screen, angle, length, width, color):
    """ Draws a hand for the clock given an angle, length, width, and color. """
    x = 200 + length * sin(radians(angle))
    y = 200 - length * cos(radians(angle))
    pygame.draw.line(screen, color, (200, 200), (x, y), width)

def calculate_angles():
    """ Calculates the angles of the hour, minute, and second hands. """
    now = datetime.now()
    second_angle = now.second * 6  # 6 degrees per second
    minute_angle = now.minute * 6 + now.second * 0.1  # 6 degrees per minute + small adjustment for seconds
    hour_angle = now.hour % 12 * 30 + now.minute * 0.5  # 30 degrees per hour + adjustment for minutes
    return hour_angle, minute_angle, second_angle

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Clear the screen with white
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate current angles
    hour_angle, minute_angle, second_angle = calculate_angles()

    # Draw the clock hands
    draw_hand(screen, hour_angle, 80, 8, (0, 0, 0))  # Hour hand
    draw_hand(screen, minute_angle, 120, 5, (0, 0, 0))  # Minute hand
    draw_hand(screen, second_angle, 140, 2, (255, 0, 0))  # Second hand

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
