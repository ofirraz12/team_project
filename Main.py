import pygame

state = {
    "state": consts.RUNNING_STATE,
    "is movement": False,
    "is_window_open": True,
}


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            pass

        if event.key == pygame.K_SPACE:
            pass
