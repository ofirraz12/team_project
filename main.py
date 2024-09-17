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
    "click_down": False,
    "click_up": False,
    "click_down_time": 0,
    "click_up_time": 0,
    "slot": 0
}


def main():
    pygame.init()
    game_field.create_grid()
    game_grid = game_field.game_grid

    while state["is_window_open"] is True:
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

        if not state["click_down"]:

            if event.type == pygame.KEYDOWN:
                state["click_down_time"] = pygame.time.get_ticks()
                state["click_down"] = True

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

                    elif event.key == pygame.K_KP_1:
                        state["slot"] = 1

                    elif event.key == pygame.K_KP_2:
                        state["slot"] = 2

                    elif event.key == pygame.K_KP_3:
                        state["slot"] = 3

                    elif event.key == pygame.K_KP_4:
                        state["slot"] = 4

                    elif event.key == pygame.K_KP_5:
                        state["slot"] = 5

                    elif event.key == pygame.K_KP_6:
                        state["slot"] = 6

                    elif event.key == pygame.K_KP_7:
                        state["slot"] = 7

                    elif event.key == pygame.K_KP_8:
                        state["slot"] = 8

                    elif event.key == pygame.K_KP_9:
                        state["slot"] = 9

        elif event.type == pygame.KEYUP:
            state["click_up_time"] = pygame.time.get_ticks()
            state["click_up"] = True

            if state["click_down"] and state["click_up"]:
                time_held = state["click_up_time"] - state["click_down_time"]
                print(state["slot"], time_held)
                state["click_up"], state["click_down"] = False, False


main()
