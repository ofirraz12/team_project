import pygame
import consts
import screen
import game_field

state = {
    "state": consts.RUNNING_STATE,
    "is movement": False,
    "is_window_open": True,
}


def main():
    game_field.create_grid()
    game_grid = game_field.game_grid
    print(game_grid[0][1])


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            pass

        if event.key == pygame.K_SPACE:
            pass


main()
