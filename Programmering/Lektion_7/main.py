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