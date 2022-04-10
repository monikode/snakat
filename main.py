import pygame
from config import INITIAL_SCREEN
from screens.game_screen import GameScreen
from screens.initial_screen import InitialScreen
from screens.config_screen import ConfigScreen

game_loop = True
SCREENS = [InitialScreen(), ConfigScreen(), GameScreen()]
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
            screen.mouse_events([0, 0, 0, 0])  # what does this mean?

    screen.main()

    if screen.state != screen_state:
        old_screen = screen
        screen = SCREENS[screen.state].screen_in()
        screen.tiles = old_screen.tiles
        screen.speed = old_screen.speed
        screen.cat_img = old_screen.cat_img
        screen.food_img = old_screen.food_img

pygame.display.quit()
pygame.quit()
