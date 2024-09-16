import pygame
import consts

def crete_screen(width,height,window_color):
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    surface.fill(window_color)