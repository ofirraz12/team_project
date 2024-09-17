from consts import *
import random
import pygame

game_grid = []


def create_grid():
    global game_grid
    game_grid = [[[j] for j in range(NUM_OF_COL)] for i in range(NUM_OF_ROW)]


def add_grass():
    grass_list = []
    temp_list = []

    while len(grass_list) < 20:
        col = random.randint(0, NUM_OF_COL - 1)
        row = random.randint(0, NUM_OF_ROW - 1)
        temp_list.append([col, row])
        if temp_list[-1] not in grass_list:
            grass_list.append([col, row])

    return grass_list


def add_mines():
    mine = "mine"
    for i in range(AMOUNT_OF_GRASS):
        col = random.randint(0, NUM_OF_COL - 1)
        row = random.randint(0, NUM_OF_ROW - 1)
        game_grid[row][col].append(mine)

    return game_grid

