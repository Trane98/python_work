import pygame
import math

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((840, 680)) # Create a window of 840x680 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

#Lave omkredsen af uret
x_start,y_start=420,340
længde=305
bredde=5
pygame.draw.circle(screen, (0, 0, 0), (x_start,y_start), længde, bredde)


x_start,y_start=420,340
længde=280
bredde=2
#Så kommmer vinkel stregerne. Første streg med 22.5 grader fremover vil der blive lagt 22.5 til
angle=math.radians(22.5) #Omregning til radianer sker her
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)#Linje bliver tegnet

#Ny linje 45 grader
angle=math.radians(45)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(67.5)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(90)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(112.5)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(135)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(157.5)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(180)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(202.5)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(225)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(247.5)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(270)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(292.5)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(315)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(337.5)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(360)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)



# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears