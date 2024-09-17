from consts import *
import game_field


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


def soldier_hit_box(soldier_index):
    upper_hit_box = []
    lower_hit_box = []
    for x in range(SOLDIER_WIDTH):
        for y in range(SOLDIER_HEIGHT):
            if y == 3:
                lower_hit_box.append([soldier_index[0] + x, soldier_index[1] + y])
            else:
                upper_hit_box.append([soldier_index[0] + x, soldier_index[1] + y])
    return [lower_hit_box, upper_hit_box]

