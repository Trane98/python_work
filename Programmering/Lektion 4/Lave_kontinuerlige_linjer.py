import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
screen.fill((255,255,255))
pygame.display.flip()

click_x=[]
click_y=[]

while True:
   for event in pygame.event.get(): #Kommandoen her indhenter oplysninger om tryk og tastning
      if event.type == pygame.QUIT: #Kommandoen her sørger for, at hvis der trykkes på luk, så indhentes oplysningen og programmet lukkes.
         pygame.quit() #Her kontrolleres om oplysningen som indhentes er luk
         sys.exit() #Hvis hændelsen er quit, så lukkes programmet her. 
      if event.type == pygame.MOUSEBUTTONDOWN: #Her kontrolleres der for museklik
         pos=pygame.mouse.get_pos() #Her registeres museklik og de gemmes så i pos i form af x og y pos[0] og pos[1]
         btn=pygame.mouse #Denne linje gemmer museobjektet fra Pygame, hvilket kan bruges til at tjekke for andre egenskaber ve
         print ("x = {}, y = {}".format(pos[0], pos[1])) #Printer koordinater for tryk. (Ikke vigtig for koden)
         click_x.append(pos[0]) #Gemmer data for sidste tryk x-akse
         click_y.append(pos[1]) #Gemmer data for sidste tryk y-ake
         
         if len(click_x) == 2 and len(click_y) == 2: #Aktivere if statement, når der er 2 elementer i click_x og click_y
            pygame.draw.line(screen, (0, 0, 0), (click_x[0], click_y[0]), (click_x[1], click_y[1])) #Laver linje med de første 2 tryk
            pygame.display.flip() #Opdatere handling
            del click_x[0] #Sletter første museklik x-akse
            del click_y[0] #Sletter første museklik y-aske
# Koden gentages, i true, men nu er sidste værdi, som blev klikket den første værdi, den gemmer altså sidste klik som første
#og sletter altid første så den gemmer sidte. På den måde, laver den hele tiden en ny linje