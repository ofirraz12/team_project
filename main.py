import pygame

import consts
from consts import *
import screen
import game_field
import soldier

state = {
    "state": RUNNING_STATE,
    "view_mines": False,
    "is_window_open": True,
    "movement": True,
}


def main():
    pygame.init()
    game_field.create_grid()
    game_grid = game_field.game_grid


    while state["is_window_open"] == True:
        handle_user_events()
        screen.draw_game(state)
        pygame.display.flip()
        game_field.got_to_flag(FLAG_LOCATION, soldier_index, state)
        game_field.steeped_on_mine(soldier.soldier_hit_box(soldier_index), screen.mines_indexes, state)


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != RUNNING_STATE:
            state["movement"] = False

        if event.type == pygame.KEYDOWN:

            if state["movement"]:
                if event.key == pygame.K_SPACE:
                    state["movement"] = False
                    state["view_mines"] = True
                    continue

                if event.key == pygame.K_LEFT:
                    soldier.move_soldier("left", soldier_index)

                elif event.key == pygame.K_RIGHT:
                    soldier.move_soldier("right", soldier_index)

                elif event.key == pygame.K_UP:
                    soldier.move_soldier("up", soldier_index)

                elif event.key == pygame.K_DOWN:
                    soldier.move_soldier("down", soldier_index)


main()
