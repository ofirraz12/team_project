
import pygame
import consts


screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()