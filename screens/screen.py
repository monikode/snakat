from asyncio.windows_events import NULL
import pygame
from config import CATS, FOODS, SCREEN_WIDTH, SCREEN_HEIGHT, SIZES, SPEED, is_clicked
from abc import ABC, abstractmethod


class Button:
    is_hovering = 0

    def __init__(self, image, x, y, width, height, onclick, click_param = None):
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclick = onclick
        self.click_param = click_param

    def draw(self, surface):
        self.is_hovering = 0

        if is_clicked(pygame.mouse.get_pos(), [self.x, self.y, self.width, self.height]):
            self.is_hovering = 1
        surface.blit(self.image, (self.x, self.y),
                     (self.is_hovering * self.width, 0, self.width, self.height))

    def click(self):
        if self.click_param != None:
            self.onclick(self.click_param)
        else:
            self.onclick()

    def set_pos(self, x, y):
        self.x = x
        self.y = y


class ScreenParams:
    def __init__(self):
        self.tiles = SIZES[0]
        self.food_img = FOODS[0]
        self.cat_img = CATS[0]
        self.speed = SPEED[1]


class Screen(ABC, ScreenParams):  # ABC stands for AbstractClass
    surface: pygame.Surface
    caption = ""
    height = SCREEN_HEIGHT
    width = SCREEN_WIDTH
    tick = 0
    transition = 10
    transition_animation = -1
    transition_direction = 0

    def __init__(self, state, index):
        ScreenParams.__init__(Screen)
        self.surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.surface.fill((255, 255, 255))
        self.state = state
        self.index = index
        self.next_state = self.state
        self.buttons = []
        self.light = pygame.Surface((self.width, self.height))
        self.points = 0
        self.high_score = 0

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

    def screen_in(self, old_screen = None):
        self.tick = 0
        self.transition_animation = 0
        self.transition_direction = 1
        self.state = self.index
        
        self.tiles = old_screen.tiles
        self.speed = old_screen.speed
        self.cat_img = old_screen.cat_img
        self.food_img = old_screen.food_img
        self.points = old_screen.points
        self.high_score = old_screen.high_score

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

    def draw_frame(self):
        self.surface.fill((255, 255, 255))

        self.light.set_alpha(300 - self.transition_animation * (300 // self.transition))
        self.light.fill((255, 255, 255))

    def is_win(self):
        return self.points == self.tiles**2 - 2
