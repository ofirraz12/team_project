import pygame
from consts import *
import game_field
import screen


def draw_soldier():
    soldier_image = pygame.image.load(SOLDIER_IMG)
    soldier_image = pygame.transform.scale(soldier_image, (SOLDIER_WIDTH * BOX_SIZE,SOLDIER_HEIGHT * BOX_SIZE))
    screen.screen.blit(soldier_image, (0, 0))
    pygame.display.flip()
