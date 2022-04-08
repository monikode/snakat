from screen import Button, Screen
from config import CONFIG_SCREEN, GAME_SCREEN, INITIAL_SCREEN, is_clicked
import pygame


class InitialScreen(Screen):
    state = INITIAL_SCREEN
    index = INITIAL_SCREEN

    def __init__(self):
        super().__init__()

        self.buttons = [
            Button("initial_button_play.png", 425, 235, 200,
                   120, lambda: self.change_screen(GAME_SCREEN)),
            Button("initial_button_personalize.png", 625, 235, 150,
                   120, lambda: self.change_screen(CONFIG_SCREEN)),
            Button("initial_button_infos.png", 1070, 10, 120,
                   120, lambda: self.change_screen(CONFIG_SCREEN)),
        ]

        self.bg = pygame.image.load("initial_page.png")

    def keyboard_events(self):
        # not implemented
        pass

    def game(self):
        # not implemented
        pass

    def draw(self):
        self.surface.fill( (255, 255, 255))

        light = pygame.Surface((self.width, self.height))
        light.set_alpha(300-self.transition_animation*(300/self.transition))
        light.fill( (255, 255, 255))

        self.buttons[0].set_pos(425 -50 + self.transition_animation*(50/self.transition),235)
        self.buttons[1].set_pos(625 +50 - self.transition_animation*(50/self.transition),235)
        self.buttons[2].set_pos(1070, 10 -50 + self.transition_animation*(50/self.transition))

        pygame.display.set_caption("Snakat - Initial")
        self.surface.blit(pygame.transform.scale(self.bg, (self.width, self.height)), (0, 0))
        self.draw_buttons()
        self.surface.blit(light, (0, 0))

