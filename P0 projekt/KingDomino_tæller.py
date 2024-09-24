import pygame
import math
from datetime import datetime


pygame.init()
screen = pygame.display.set_mode((840, 680))

while True:
    second_length=255
    minute_length=240
    hour_length=150
    width = 2
    screen.fill((255,255,255))
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
    pygame.draw.line(screen, (255, 0, 0), (x_start, y_start), (x_end_second, y_end_second), 2)  #Sekundviseren
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end_minute, y_end_minute), 4)  #Minutviseren
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end_hour, y_end_hour), 6)  #Timeviseren

    #Laver alle tallene til uret
    angle=30
    for i in range(0,12):
        font = pygame.font.Font(None, 60)
        længde=280
        bredde=5
        angle_radient = math.radians(i*angle-60)
        text_surface = font.render(f"{1+i}", True, (0, 0, 0))
        x_end = x_start + længde * math.cos(angle_radient) - text_surface.get_width() // 2 
        y_end = y_start + længde * math.sin(angle_radient) - text_surface.get_height() // 2
        screen.blit(text_surface, (x_end, y_end))
    
    længde_cirkel=320
    bredde_cirkel=4
    #Laver cirklen
    pygame.draw.circle(screen, (0, 0, 0), (x_start,y_start), længde_cirkel, bredde_cirkel)

    #Test af linjer i kanten af cirklen
    længde=12
    radius=305
    for i in range(6,366,6):
        angle=math.radians(i)
        x_start=420+radius*math.cos(angle)
        y_start=340+radius*math.sin(angle)

        x_end=x_start+længde*math.cos(angle)