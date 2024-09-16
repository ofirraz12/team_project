import pygame
import consts
import random as r

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()


def draw_grass(game_grid):
    image = pygame.image.load("grass.png")
