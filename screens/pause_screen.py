from screens.screen import Screen, Button
from config import PAUSE_SCREEN, GAME_SCREEN, CONFIG_SCREEN, INITIAL_SCREEN
import pygame


class PauseScreen(Screen):
    def __init__(self):
        super().__init__(PAUSE_SCREEN, PAUSE_SCREEN)

        self.buttons = [
            Button("imgs/button_resume.png", 900, 900, 250, 100,
                   lambda: self.change_screen(GAME_SCREEN)),
            Button("imgs/button_reset.png", 400, 500, 191, 100,
                   self.reset_game),
            Button("imgs/button_config.png", 400, 500, 88, 85,
                   self.to_config),
        ]

        self.bg = pygame.image.load("imgs/pause_bg.png")

    def keyboard_events(self):
        #do nothing
        pass

    def reset_game(self):
        self.paused = False
        self.change_screen(GAME_SCREEN)

    def to_config(self):
        self.paused = False
        self.change_screen(CONFIG_SCREEN)

    def game(self):
        #do nothing
        pass

    def draw(self):
        super().draw_frame()

        self.buttons[0].set_pos(
            485 - 50 + self.transition_animation * (50 / self.transition), 300)
        self.buttons[1].set_pos(
            465 + 50 - self.transition_animation * (50 / self.transition), 400)
        self.buttons[2].set_pos(
            665 + 50 - self.transition_animation * (50 / self.transition), 400)

        pygame.display.set_caption("Snakat - Pause")
        self.surface.blit(pygame.transform.scale(
            self.bg, (self.width, self.height)), (0, 0))
        self.draw_buttons()
        self.surface.blit(self.light, (0, 0))

