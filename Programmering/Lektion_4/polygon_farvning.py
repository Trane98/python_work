import pygame, sys
import random


pygame.init()
screen = pygame.display.set_mode((840, 680))
pygame.display.set_caption("Hello World")
screen.fill((255,255,255))
pygame.display.flip()

random_number0 = random.randint(0,255)
random_number1 = random.randint(0,255)
random_number2 = random.randint(0,255)
x_click=[]
y_click=[]


while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         pos=pygame.mouse.get_pos()
         btn=pygame.mouse
         x_click.append(pos[0])
         y_click.append(pos[1])
         if len(x_click) == 3 and len(y_click) == 3:
            random_number0 = random.randint(0,255)
            random_number1 = random.randint(0,255)
            random_number2 = random.randint(0,255)
            pygame.draw.polygon(screen,(random_number0,random_number1,random_number2),[(x_click[0],y_click[0]),(x_click[1],y_click[1]),(x_click[2],y_click[2])])
            pygame.display.flip()
            print ("x = {}, y = {}".format(pos[0], pos[1]))
            x_click.clear()
            y_click.clear()