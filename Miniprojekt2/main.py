import pygame,sys

def start_pygame(screen_size):
    """Start Pygame og sætter op en skærm"""
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    return screen

def handle_event_exit():
    """Handler for events som at lukke spillet"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False  # Returnér False for at stoppe spillet
    return True  # Fortsæt spillet ellers


def update_screen(screen, color):
    """Opdatere skærmen"""
    screen.fill(color)
    pygame.display.flip()


def create_grid_64x48():
    """Laver en liste med 64x48 0'er"""
    grid_64x48 = [[0 for row in range(48)] for col in range(64)]
    return grid_64x48



class Terrain_Types:
    def __init__(self, color, grid_number):
        self.color = color
        self.grid_number = grid_number

