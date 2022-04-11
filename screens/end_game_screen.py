from screens.screen import Screen, Button
from config import PAUSE_SCREEN, GAME_SCREEN, CONFIG_SCREEN
import pygame

class EndGameScreen(Screen):
    def __init__(self):
        super().__init__(PAUSE_SCREEN, PAUSE_SCREEN)

        self.buttons = [
            Button("imgs/button_play_again.png", 900, 900, 250, 100, lambda: self.change_screen(GAME_SCREEN)),
            Button("imgs/button_config.png", 400, 500, 88, 85, lambda: self.change_screen(CONFIG_SCREEN)),
        ]

        self.bg = pygame.image.load("imgs/game_over_bg.png")

    def keyboard_events(self):
        pass

    def game(self):
        pass

    def draw(self):
        super().draw_frame()

        self.buttons[0].set_pos(410 - 50 + self.transition_animation * (50 / self.transition), 430)
        self.buttons[1].set_pos(675 + 50 - self.transition_animation * (50 / self.transition), 430)

        pygame.display.set_caption("Snakat - Game Over")
        self.surface.blit(pygame.transform.scale(self.bg, (self.width, self.height)), (0, 0))
        self.draw_buttons()
        self.surface.blit(self.light, (0, 0))
    
    def screen_in(self, old_screen):
        self = super().screen_in(old_screen)
        self.food_img = old_screen.food_img
        self.points = old_screen.points
        self.tiles = old_screen.tiles
        
        if self.points == (self.tiles**2 - 2):
            self.bg = pygame.image.load("imgs/game_over_win_bg.png")

        return self