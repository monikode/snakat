from screen import Button, Screen
from config import CONFIG_SCREEN, GAME_SCREEN, INITIAL_SCREEN
import pygame


class InitialScreen(Screen):
    def __init__(self):
        super().__init__(INITIAL_SCREEN, INITIAL_SCREEN)

        self.buttons = [
            Button("imgs/initial_button_play.png", 425, 235, 200,
                   120, lambda: self.change_screen(GAME_SCREEN)),
            Button("imgs/initial_button_personalize.png", 625, 235, 150,
                   120, lambda: self.change_screen(CONFIG_SCREEN)),
            Button("imgs/initial_button_infos.png", 1070, 10, 120,
                   120, lambda: self.change_screen(CONFIG_SCREEN)),
        ]

        self.bg = pygame.image.load("imgs/initial_page.png")

    def keyboard_events(self):
        # not implemented
        pass

    def game(self):
        # not implemented
        pass

    def draw(self):
        super().draw_frame()

        self.buttons[0].set_pos(425 - 50 + self.transition_animation*(50/self.transition), 235)
        self.buttons[1].set_pos(625 + 50 - self.transition_animation*(50/self.transition), 235)
        self.buttons[2].set_pos(1070, 10 - 50 + self.transition_animation*(50/self.transition))

        pygame.display.set_caption("Snakat - Initial")
        self.surface.blit(pygame.transform.scale(self.bg, (self.width, self.height)), (0, 0))
        self.draw_buttons()
        self.surface.blit(self.light, (0, 0))
