from consts import *
def create_grid():
    game_grid = [[[j] for j in range(NUM_OF_ROW)] for i in range(NUM_OF_COL)]
    print(game_grid)