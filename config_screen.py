from screen import Button, Screen
from config import CONFIG_SCREEN, INITIAL_SCREEN, is_clicked
import pygame


class ConfigScreen(Screen):
    state = CONFIG_SCREEN
    index = CONFIG_SCREEN
    cube_color = (234, 12, 139)

    def __init__(self):
        super().__init__()
        self.cube = [self.width/2, self.height/2, 40, 40]
        self.buttons = [
            Button("initial_button_infos.png", 1070, 10, 120,
                   120, lambda: self.change_screen(INITIAL_SCREEN)),
        ]

    def mouse_events(self, pos):
        super().mouse_events(pos)
        if is_clicked(pos, self.cube):
            self.cube_color = (0, 0, 0)
        else:
            self.cube_color = (234, 12, 139)

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

        pygame.display.set_caption("Snakat - Config")
        pygame.draw.rect(self.surface, (12, 242, 9), [
                         0, 0, self.width, self.height])
        pygame.draw.rect(self.surface, self.cube_color, self.cube)
        self.draw_buttons()
        self.surface.blit(light, (0, 0))
