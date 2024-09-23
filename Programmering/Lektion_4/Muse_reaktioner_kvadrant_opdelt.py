import pygame, sys

#Boiler plate start
pygame.init()
screen = pygame.display.set_mode((840, 680))
pygame.display.set_caption("Hello World")
screen.fill((255,255,255)) #Farver skærmen hvid i starten af programmet
pygame.display.flip() #Aktiverer starten og viser den hvide skærm

while True:
   for event in pygame.event.get(): #Kommandoen her indhenter oplysninger om tryk og tastning
      if event.type == pygame.QUIT: #Kommandoen her sørger for, at hvis der trykkes på luk, så indhentes oplysningen og programmet lukkes.
         pygame.quit() #Her kontrolleres om oplysningen som indhentes er luk
         sys.exit() #Hvis hændelsen er quit, så lukkes programmet her. 
      if event.type == pygame.MOUSEBUTTONDOWN: #Her kontrolleres der for museklik
         pos=pygame.mouse.get_pos() #Her registeres museklik og de gemmes så i pos i form af x og y pos[0] og pos[1]
         btn=pygame.mouse #Denne linje gemmer museobjektet fra Pygame, hvilket kan bruges til at tjekke for andre egenskaber ved musen

# 2 kvadrant
         if 0 <= pos[0] <= 420 and 0 <= pos[1] <= 340: #Hvis x er mellem 0 og 420 og y er mellem 0 og 340, så aktiveres koden under
            pygame.draw.circle(screen,(255,0,255),(pos[0],pos[1]),20) # Laver en cirkel med en given farvekode. 
            print ("x = {}, y = {}".format(pos[0], pos[1])) # Kommandoen her bruges til at sige, hvor der trykkes
            pygame.display.flip() # Alt der aktivt laves opdateres på skærmen. 

# 1 kvadrant
         elif 420 <= pos[0] <=840 and 0 <= pos[1] <= 340:
            pygame.draw.circle(screen,(0,255,255),(pos[0],pos[1]),20)
            print ("x = {}, y = {}".format(pos[0], pos[1]))
            pygame.display.flip()

# 3 kvadrant
         elif 0 <= pos[0] <= 420 and 340 <= pos[1] <= 680:
            pygame.draw.circle(screen,(255,255,0),(pos[0],pos[1]),20)
            print ("x = {}, y = {}".format(pos[0], pos[1]))
            pygame.display.flip()

# 4 kvadrant
         elif 420 <= pos[0] <=840 and 340 <= pos[1] <=680:
            pygame.draw.circle(screen,(0,0,0),(pos[0],pos[1]),20)
            print ("x = {}, y = {}".format(pos[0], pos[1]))
            pygame.display.flip()