import pygame
import math
from datetime import datetime


pygame.init()
screen = pygame.display.set_mode((840, 680))

#While loop til uret
while True:
    #Laver baggrund til uret
    imp = pygame.image.load("C:\\Program Files (x86)\\python_work\\python_work\\Miniprojekt1.py\\Ur_billede.png")
    screen.blit(imp, (-102, -150))


#################################################################### Omhandler viserne nedenunder ####################################################################

    second_length=240
    minute_length=225
    hour_length=140
    x_start, y_start = 420, 340

    #Importere den nuværende tid.
    current_time = datetime.now()

    #Udregner vinklerne for de 3 visere
    second_angle = math.radians((current_time.second/60)*360)
    minute_angle = math.radians((current_time.minute/60)*360)
    hour_angle = math.radians(((current_time.hour%12)/12)*360+(current_time.minute / 60) * 30)

    #Udregner hvor ende koordinaterne er i sekundviseren
    x_end_second = x_start + second_length * math.cos(second_angle - math.pi / 2)
    y_end_second = y_start + second_length * math.sin(second_angle - math.pi / 2)

    #Udregner hvor ende koordinaterne er i minutviseren
    x_end_minute = x_start + minute_length * math.cos(minute_angle - math.pi / 2)
    y_end_minute = y_start + minute_length * math.sin(minute_angle - math.pi / 2)

    #Udregner hvor ende koordinaterne er i timeviseren
    x_end_hour = x_start + hour_length * math.cos(hour_angle - math.pi / 2)
    y_end_hour = y_start + hour_length * math.sin(hour_angle - math.pi / 2)

    #Tegner sekund, minut og time viseren
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end_hour, y_end_hour), 8)  #Timeviseren
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end_minute, y_end_minute), 6)  #Minutviseren
    pygame.draw.line(screen, (0, 205, 255), (x_start, y_start), (x_end_second, y_end_second), 4)  #Sekundviseren
#################################################################### Omhandler viserne ovenover ####################################################################



#################################################################### Laver tallene til uret nedenunder ####################################################################

    angle=30
    for i in range(0,12):
        font = pygame.font.Font(None, 60)
        length_number=270
        angle_radient = math.radians(i*angle-60)
        text_surface = font.render(f"{1+i}", True, (0, 0, 0))
        x_end = x_start + length_number * math.cos(angle_radient) - text_surface.get_width() // 2 
        y_end = y_start + length_number * math.sin(angle_radient) - text_surface.get_height() // 2
        screen.blit(text_surface, (x_end, y_end))

#################################################################### Laver tallene til uret ovenover ####################################################################
    


#################################################################### Laver cirklen af uret nedenunder ####################################################################
    length_cirkel=315
    width_cirkel=8
    #Laver cirklen
    pygame.draw.circle(screen, (0, 0, 0), (x_start,y_start), length_cirkel, width_cirkel)

#################################################################### Laver cirklen af uret ovenover ####################################################################



#################################################################### Laver linjer til uret 60x linjer nedenunder ####################################################################

    #Linjer i kanten af cirklen
    længde_linjer_til_skive=12
    radius_linjer_til_skive=295
    for i in range(6,366,6):
        angle=math.radians(i)
        x_start=420+radius_linjer_til_skive*math.cos(angle)
        y_start=340+radius_linjer_til_skive*math.sin(angle)

        x_end=x_start+længde_linjer_til_skive*math.cos(angle)
        y_end=y_start+længde_linjer_til_skive*math.sin(angle)
        pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end),4)

    pygame.display.flip()

#################################################################### Laver linjer til uret 60x linjer ovenover ####################################################################
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()