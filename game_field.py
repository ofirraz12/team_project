from consts import *

game_grid = []


def create_grid():
    global game_grid
    game_grid = [[[j] for j in range(NUM_OF_COL)] for i in range(NUM_OF_ROW)]
