import pygame
from config import INITIAL_SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, SIZES, is_clicked
from abc import ABC, abstractmethod


class Button:
    is_hovering = 0

    def __init__(self, image, x, y, width, height, onclick):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclick = onclick

    def draw(self, surface):
        self.is_hovering = 0

        if is_clicked(pygame.mouse.get_pos(), [self.x, self.y, self.width, self.height]):
            self.is_hovering = 1
        surface.blit(self.image, (self.x, self.y),
                     (self.is_hovering * self.width, 0, self.width, self.height))

    def click(self):
        self.onclick()

    def set_pos(self, x, y):
        self.x = x
        self.y = y


class ScreenParams:
    tiles = SIZES[0]


class Screen(ABC, ScreenParams):
    surface: pygame.Surface
    caption = ""
    height = SCREEN_HEIGHT
    width = SCREEN_WIDTH
    tick = 0
    transition = 10
    transition_animation = -1
    transition_direction = 0

    def __init__(self):
        ScreenParams().__dict__
        self.surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.surface.fill((255, 255, 255))
        self.next_state = self.state
        self.buttons = []

    def mouse_events(self, pos):
        for button in self.buttons:
            if is_clicked(pos, [button.x, button.y, button.width, button.height]):
                button.click()

    @abstractmethod
    def keyboard_events(self):
        pass

    @abstractmethod
    def game(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

    def main(self):

        self.keyboard_events()
        self.game()
        self.draw()
        pygame.display.flip()
        self.tick += 1
        self.transition_animation += self.transition_direction
        if self.transition_animation == 0 or self.transition_animation == self.transition:
            if self.transition_direction == -1:
                self.state = self.next_state
            self.transition_direction = 0

    def change_screen(self, state):
        self.next_state = state
        self.transition_animation = self.transition
        self.transition_direction = -1

    def screen_in(self):
        self.tick = 0
        self.transition_animation = 0
        self.transition_direction = 1
        self.state = self.index
        return self

    def screen_out(self):
        return self

    def draw_buttons(self):
        hovering = 0
        for button in self.buttons:
            button.draw(self.surface)
            hovering += button.is_hovering

        if hovering > 0:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
