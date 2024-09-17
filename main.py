import pygame
from consts import *
import screen
import game_field
import soldier

state = {
    "state": RUNNING_STATE,
    "view_mines": False,
    "is_window_open": True,
}


def main():
    pygame.init()
    game_field.create_grid()
    game_grid = game_field.game_grid

    while state["is_window_open"] == True:
        handle_user_events()
        screen.draw_game(state)
        pygame.display.flip()


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != RUNNING_STATE:
            pass

        if state["view_mines"] == True:
            pass

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                print("space was pressed")

            elif event.key == pygame.K_LEFT:
                soldier.move_soldier("left", soldier_index)
                print("left was pressed")

            elif event.key == pygame.K_RIGHT:
                soldier.move_soldier("right", soldier_index)
                print("right was pressed")

            elif event.key == pygame.K_UP:
                soldier.move_soldier("up", soldier_index)
                print("up was pressed")

            elif event.key == pygame.K_DOWN:
                soldier.move_soldier("down", soldier_index)
                print("down was pressed")


main()
