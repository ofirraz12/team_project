from consts import *
import random
import pygame

game_grid = []


def create_grid():
    global game_grid
    game_grid = [[[j] for j in range(NUM_OF_COL)] for i in range(NUM_OF_ROW)]

def draw_grass(game_grid):
    image = pygame.image.load("grass.png")
    x = random.randint(0,NUM_OF_COL - 1)
    y = random.randint(0,NUM_OF_ROW - 1)