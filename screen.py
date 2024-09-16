import pygame
from consts import *


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_game(game_state):
    screen.fill(BACKGROUND_COLOR)


def draw_grass(grass_indexes):
    grass = pygame.image.load(GRASS_IMG)
    grass = pygame.transform.scale(grass, (BOX_SIZE * 2, BOX_SIZE * 2))

    for index in grass_indexes:
        screen.blit(grass.convert_alpha(), (index[0] * BOX_SIZE, index[1] * BOX_SIZE))
