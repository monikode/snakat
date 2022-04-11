from screens.screen import Button, Screen
from config import CONFIG_SCREEN, GAME_SCREEN, INITIAL_SCREEN
import pygame
pygame.mixer.init()

class InitialScreen(Screen):
    def __init__(self):
        super().__init__(INITIAL_SCREEN, INITIAL_SCREEN)
        self.buttons = [
            Button("imgs/button_play.png", 425, 235, 191,
                   85, lambda: self.change_screen(GAME_SCREEN)),
            Button("imgs/button_config.png", 625, 235, 88,
                   85, lambda: self.change_screen(CONFIG_SCREEN)),
        ]

        self.bg = pygame.image.load("imgs/initial_page.png")
        self.logo = pygame.image.load("imgs/logo.png")
        pygame.mixer.music.load("sounds/menu_cat.mp3")
        pygame.mixer.music.play(-1, 0, 0)

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

        pygame.display.set_caption("Snakat - Initial")
        self.surface.blit(pygame.transform.scale(self.bg, (self.width, self.height)), (0, 0))
        self.draw_buttons()
        self.surface.blit(self.logo, (425, 40))
        self.surface.blit(self.light, (0, 0))
