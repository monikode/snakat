import pygame
from config import INITIAL_SCREEN
from screens.game_screen import GameScreen
from screens.initial_screen import InitialScreen
from screens.config_screen import ConfigScreen
from screens.pause_screen import PauseScreen

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
        screen = SCREENS[screen.state].screen_in(old_screen)
        
pygame.display.quit()
pygame.quit()
 
