from consts import *


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


