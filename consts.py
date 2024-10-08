import pygame

NUM_OF_ROW = 25
NUM_OF_COL = 50
NUM_OF_GRASS = 20
NUM_OF_MINES = 20
BOX_SIZE = 25

GRASS_IMG = r"photos\grass.png"
SOLDIER_IMG = r"photos\soldier.png"
SOLDIER_NIGHT_IMG = r"photos\soldier_nigth.png"
SOLDIER_INJURED_IMG = r"photos\injury.png"
FLAG_IMG = r"photos\flag.png"
MINE_IMG = r"photos\mine.png"
EXPLOTION_IMG = r"photos\explotion.png"

WINDOW_WIDTH = NUM_OF_COL * BOX_SIZE
WINDOW_HEIGHT = NUM_OF_ROW * BOX_SIZE

BACKGROUND_COLOR = (38, 155, 38)
VIEW_MINES_COLOR = (0, 0, 0)

SOLDIER_WIDTH = 2
SOLDIER_HEIGHT = 4
SOLDIER_START_X, SOLDIER_START_Y = 0, 0
soldier_index = [SOLDIER_START_X, SOLDIER_START_Y]

MINE_WIDTH = 3
MINE_HEIGHT = 1

FLAG_WIDTH = 4
FLAG_HEIGHT = 3
FLAG_LOCATION = [NUM_OF_COL - FLAG_WIDTH, NUM_OF_ROW - FLAG_HEIGHT]

FONT_NAME = "Calibri"
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = (0, 0, 0)
LOSE_LOCATION = (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (0, 0, 0)
WIN_LOCATION = (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3
PLAY_AGAIN_STATE = 4