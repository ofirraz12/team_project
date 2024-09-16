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
    pygame.init()
    game_field.create_grid()
    game_grid = game_field.game_grid

    while state["is_window_open"] == True:
        handle_user_events()
        screen.draw_game(state)


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            pass

        if state["is movement"] == True:
            pass

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                print("space was pressed")

            elif event.key == pygame.K_LEFT:
                print("left was pressed")

            elif event.key == pygame.K_RIGHT:
                print("right was pressed")

            elif event.key == pygame.K_UP:
                print("up was pressed")

            elif event.key == pygame.K_DOWN:
                print("down was pressed")


main()
