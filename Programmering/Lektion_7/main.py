import pygame,sys

def start_pygame(screen_size):
    """Start Pygame og sætter op en skærm"""
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    return screen

def handle_event_exit():
    """Handler for events som at slukke spillet"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        return True

def update_screen(screen, color):
    """Opdatere skærmen"""
    screen.fill(color)
    pygame.display.flip()


def create_grid_64x48():
    """Laver en liste med 64x48 0'er"""
    template_for_64x48 = []

    for _ in range(64):
        template_for_64x48.append(0)

    grid_function = []
    for _ in range(48):
        grid_function.append(template_for_64x48.copy()) #Laver en række, som er en seperat liste

    return grid_function


def draw_horizontal(grid, y, x_start, x_end):
    """Tegner en vandret linje fra x_start til x_end på rækken y"""
    if x_start > x_end:
        x_start, x_end = x_end, x_start

    for i in range(x_start, x_end + 1): #Plus en er med for at sikre, at slutværdien inkluderes i løkken
        grid[y][i] = 1

    return grid

def draw_vertical(grid, x, y_start, y_end):
    """Tegner en lodret linje fra y_start til y_end på kolonnen x"""
    if y_start > y_end:
        y_start, y_end = y_end, y_start
    
    for i in range(y_start, y_end + 1):
        grid[i][x] = 1
