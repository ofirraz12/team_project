import pygame
from consts import *
import game_field
import time

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
grass_indexes = game_field.add_grass()
mines_indexes = game_field.add_mines()


def draw_game(state):
    if state["state"] == RUNNING_STATE:
        screen.fill(BACKGROUND_COLOR)
        draw_grass(grass_indexes)
        draw_soldier(soldier_index, "normal")
        draw_flag()

        if state["view_mines"]:
            screen.fill(VIEW_MINES_COLOR)
            for i in range(1, NUM_OF_COL):
                pygame.draw.line(screen, BACKGROUND_COLOR, (i * BOX_SIZE, 0), (i * BOX_SIZE, NUM_OF_ROW * BOX_SIZE)
                                 , width=2)

            for j in range(1, NUM_OF_ROW):
                pygame.draw.line(screen, BACKGROUND_COLOR, (0, j * BOX_SIZE), (NUM_OF_COL * BOX_SIZE, j * BOX_SIZE)
                                 , width=2)

            draw_mines(mines_indexes)
            draw_soldier(soldier_index, "night")
            pygame.display.flip()
            time.sleep(1)
            state["movement"] = True
            pygame.event.clear()
            state["view_mines"] = False

    elif state["state"] == WIN_STATE:
        draw_win_message()

    elif state["state"] == LOSE_STATE:
        draw_lose_message()


def draw_grass(indexes):
    grass = pygame.image.load(GRASS_IMG)
    grass = pygame.transform.scale(grass, (BOX_SIZE * 2, BOX_SIZE * 2))

    for index in indexes:
        screen.blit(grass.convert_alpha(), (index[0] * BOX_SIZE, index[1] * BOX_SIZE))


def draw_soldier(index, type_s):
    if type_s == "normal":
        soldier_image = pygame.image.load(SOLDIER_IMG)
        soldier_image = pygame.transform.scale(soldier_image, (SOLDIER_WIDTH * BOX_SIZE, SOLDIER_HEIGHT * BOX_SIZE))
        screen.blit(soldier_image, (index[0] * BOX_SIZE, index[1] * BOX_SIZE))

    elif type_s == "night":
        soldier_image = pygame.image.load(SOLDIER_NIGHT_IMG)
        soldier_image = pygame.transform.scale(soldier_image, (SOLDIER_WIDTH * BOX_SIZE, SOLDIER_HEIGHT * BOX_SIZE))
        screen.blit(soldier_image, (index[0] * BOX_SIZE, index[1] * BOX_SIZE))


def draw_flag():
    flag = pygame.image.load(FLAG_IMG)
    flag = pygame.transform.scale(flag, (FLAG_WIDTH * BOX_SIZE, FLAG_HEIGHT * BOX_SIZE))
    screen.blit(flag, (FLAG_LOCATION[0] * BOX_SIZE, FLAG_LOCATION[1] * BOX_SIZE))


def draw_mines(indexes):
    mine = pygame.image.load(MINE_IMG)
    mine = pygame.transform.scale(mine, (BOX_SIZE * MINE_WIDTH, BOX_SIZE * MINE_HEIGHT))

    for index in indexes:
        screen.blit(mine.convert_alpha(), (index[0] * BOX_SIZE, index[1] * BOX_SIZE))


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_lose_message():
    draw_message(LOSE_MESSAGE, LOSE_FONT_SIZE,
                 LOSE_COLOR, LOSE_LOCATION)


def draw_win_message():
    draw_message(WIN_MESSAGE, WIN_FONT_SIZE,
                 WIN_COLOR, WIN_LOCATION)


