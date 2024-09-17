import soldier
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

    while len(grass_list) < NUM_OF_GRASS:
        col = random.randint(1, NUM_OF_COL - 1)
        row = random.randint(1, NUM_OF_ROW - 1)
        temp_list.append([col, row])
        if temp_list[-1] not in grass_list:
            grass_list.append([col, row])

    return grass_list


def add_mines():
    mines_list = []
    temp_list = []

    while len(mines_list) < NUM_OF_MINES:
        col = random.randint(2, NUM_OF_COL - MINE_WIDTH)
        row = random.randint(3, NUM_OF_ROW - MINE_HEIGHT)
        temp_list.append([col, row])
        if temp_list[-1] not in mines_list:
            mines_list.append([col, row])

    return mines_list


def flag_hit_box(flag_location):
    flag_box = []
    for x in range(0, FLAG_HEIGHT):
        for y in range(0, FLAG_WIDTH):
            flag_box.append([flag_location[0] + x, flag_location[1] + y])
    # print(flag_box)

    return flag_box


def got_to_flag(flag_location, soldier_location, state):
    for index in soldier.soldier_hit_box(soldier_location)[1]:
        if index in flag_hit_box(flag_location):
            state["state"] = WIN_STATE


def steeped_on_mine(soldier_hit_box, mines_indexes, state):
    for box in soldier_hit_box[0]:
        for mine in mines_indexes:
            if box[1] == mine[1]:
                if mine[0] - box[0] > -1 * MINE_WIDTH and mine[0] - box[0] <= 0:
                    state["state"] = LOSE_STATE
