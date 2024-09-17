import pygame
from consts import *
import game_field


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
grass_indexes = game_field.add_grass()


def draw_game(state):
    screen.fill(BACKGROUND_COLOR)
    draw_grass(grass_indexes)
    draw_soldier(soldier_index)
    draw_flag()
    if state["view_mines"]:
        screen.fill(VIEW_MINES_COLOR)
        pygame.draw.line(screen, BACKGROUND_COLOR, (0, 0), (200, 200))


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



