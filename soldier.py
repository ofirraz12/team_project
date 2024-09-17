import pygame
from consts import *
import game_field
import screen


def draw_soldier(index):
    soldier_image = pygame.image.load(SOLDIER_IMG)
    soldier_image = pygame.transform.scale(soldier_image, (SOLDIER_WIDTH * BOX_SIZE,SOLDIER_HEIGHT * BOX_SIZE))
    screen.screen.blit(soldier_image, (index[0] * BOX_SIZE, index[1] * BOX_SIZE))
    pygame.display.flip()

def move_soldier(direction, soldier_index):
    if direction == 'left':
        if soldier_index[0] > 0:
            soldier_index[0] -= 1

    if direction == 'right':
        if soldier_index[0] + 2 < NUM_OF_COL:
            soldier_index[0] += 1

    if direction == 'up':
        if soldier_index[1] > 0:
            soldier_index[1] -= 1

    if direction == 'down':
        if soldier_index[1] + 4 < NUM_OF_ROW:
            soldier_index[1] += 1

    return soldier_index


