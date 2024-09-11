import pygame
import math

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((840, 680)) # Create a window of 840x680 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

#Lave omkredsen af uret
x_start,y_start=420,340
længde=315
bredde=5
pygame.draw.circle(screen, (0, 0, 0), (x_start,y_start), længde, bredde)


x_start,y_start=420,340
længde=255
bredde=2

#Ny linje 45 grader
angle=math.radians(30)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(60)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(90)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(120)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(150)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(180)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(210)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(240)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(270)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(300)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(330)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)

angle=math.radians(360)
x_end=x_start+længde*math.cos(angle)
y_end=y_start+længde*math.sin(angle)
pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),bredde)


#Test af tal til uret
font = pygame.font.Font(None, 60) #Skrive modul til tekst, tallet definere skriftstørrelse
x_start,y_start=420,340 #Center af uret
længde = 280 #Distancen fra midten og ud til, hvor teksten skal befinde sig
angle = math.radians(30) #laver vinkel om til radianer
text_surface = font.render("4", True, (0, 0, 0)) #Definere farve og tekst

#Beregning af tekstens position
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
#Ekstra funktionen med at dividere width og height er vigtig da tallenes position ellers vil være forskudt til at de bliver indsat i hjørnet
#Hvilket vil få dem til at stå helt forkert i forhold til pilene. 

#Få teksten over på pygame skærmen
screen.blit(text_surface, (x_end, y_end))


#Proces gentages for alle 12 tal til uret
font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(60)
text_surface = font.render("5", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(90)
text_surface = font.render("6", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(120)
text_surface = font.render("7", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(150)
text_surface = font.render("8", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(180)
text_surface = font.render("9", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(210)
text_surface = font.render("10", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(240)
text_surface = font.render("11", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(270)
text_surface = font.render("12", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(300)
text_surface = font.render("1", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(330)
text_surface = font.render("2", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))

font = pygame.font.Font(None, 60)
x_start,y_start=420,340
længde = 280 
angle = math.radians(360)
text_surface = font.render("3", True, (0, 0, 0))
x_end = x_start + længde * math.cos(angle) - text_surface.get_width() // 2 
y_end = y_start + længde * math.sin(angle) - text_surface.get_height() // 2
screen.blit(text_surface, (x_end, y_end))






# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears