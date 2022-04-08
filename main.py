import pygame
from config import CONFIG_SCREEN, INITIAL_SCREEN, GAME_SCREEN
from game_screen import GameScreen
from initial_screen import InitialScreen
from config_screen import ConfigScreen

game_loop = True
'SCREENS = [InitialScreen(), ConfigScreen(), GameScreen()]
screen = SCREENS[INITIAL_SCREEN].screen_in()
screen_state = INITIAL_SCREEN

pygame.init()


while game_loop:
    screen_state = screen.state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.MOUSEBUTTONUP:
            screen.mouse_events(pygame.mouse.get_pos())
        else:
            screen.mouse_events([0, 0, 0, 0])

    screen.main()

    if screen.state != screen_state:
        screen = SCREENS[screen.state].screen_in()


pygame.display.quit()
pygame.quit()
