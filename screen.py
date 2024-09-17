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


def draw_soldier(index):
    soldier_image = pygame.image.load(SOLDIER_IMG)
    soldier_image = pygame.transform.scale(soldier_image, (SOLDIER_WIDTH * BOX_SIZE, SOLDIER_HEIGHT * BOX_SIZE))
    screen.blit(soldier_image, (index[0] * BOX_SIZE, index[1] * BOX_SIZE))


def draw_flag():
    flag = pygame.image.load(FLAG_IMG)
    flag = pygame.transform.scale(flag, (FLAG_WIDTH * BOX_SIZE, FLAG_HEIGHT * BOX_SIZE))
    screen.blit(flag, (FLAG_LOCATION[0] * BOX_SIZE, FLAG_LOCATION[1] * BOX_SIZE))



