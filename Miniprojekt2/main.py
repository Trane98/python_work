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
    grid_64x48 = [[0 for col in range(64)] for row in range(48)]
    return grid_64x48



def draw_horizontal_water(grid, row, start_col, end_col):
    """Vandret, ændrer fx række 10, fra kolonne 5 til 15"""
    for col in range(start_col, end_col + 1): #Plus 1 skyldes at det vil give det rigtige antal, så man ikke skal tænke på at sætte ekstra ind
        grid[row][col] = 1  # Sætter 1-taller fra kolonne 5 til 15 i række 10


def draw_vertical_water(grid, col, start_row, end_row):
    """Lodret, ændrer fx kolonne 20 fra række 5 til 15"""
    for row in range(start_row, end_row + 1): #Plus 1 skyldes at det vil give det rigtige antal, så man ikke skal tænke på at sætte ekstra ind
        grid[row][col] = 1  # Sætter 1-taller fra række 5 til 15 i kolonne 20



def draw_horizontal_stone(grid, row, start_col, end_col):
    """Vandret, ændrer fx række 10, fra kolonne 5 til 15"""
    for col in range(start_col, end_col + 2): #Plus 1 skyldes at det vil give det rigtige antal, så man ikke skal tænke på at sætte ekstra ind
        grid[row][col] = 2  # Sætter 1-taller fra kolonne 5 til 15 i række 10


def draw_vertical_stone(grid, col, start_row, end_row):
    """Lodret, ændrer fx kolonne 20 fra række 5 til 15"""
    for row in range(start_row, end_row + 2): #Plus 1 skyldes at det vil give det rigtige antal, så man ikke skal tænke på at sætte ekstra ind
        grid[row][col] = 2  # Sætter 1-taller fra række 5 til 15 i kolonne 20