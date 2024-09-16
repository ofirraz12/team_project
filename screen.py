import pygame
import consts


def create_screen(width, height, window_color):
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    surface.fill(window_color)
    pygame.display.flip()


create_screen(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT, consts.WINDOW_COLOR)
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

