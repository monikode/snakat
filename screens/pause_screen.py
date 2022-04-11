from screens.screen import Screen, Button
from config import PAUSE_SCREEN, GAME_SCREEN,CONFIG_SCREEN, INITIAL_SCREEN
import pygame

class PauseScreen(Screen):
    def __init__(self):
        super().__init__(PAUSE_SCREEN, PAUSE_SCREEN)

        self.buttons = [
            Button("imgs/button_play.png", 900, 900, 191, 100, lambda: self.change_screen(GAME_SCREEN)),
            Button("imgs/button_play.png", 400, 500, 191, 100, lambda: self.change_screen(INITIAL_SCREEN)),
        ]

        self.bg = pygame.image.load("imgs/pause_bg.png")

    def keyboard_events(self):
        pass

    def game(self):
        pass

    def draw(self):
        super().draw_frame()

        self.buttons[0].set_pos(510 - 50 + self.transition_animation * (50 / self.transition), 300)
        self.buttons[1].set_pos(510 + 50 - self.transition_animation * (50 / self.transition), 400)

        pygame.display.set_caption("Snakat - Pause")
        self.surface.blit(pygame.transform.scale(self.bg, (self.width, self.height)), (0, 0))
        self.draw_buttons()
        self.surface.blit(self.light, (0, 0))