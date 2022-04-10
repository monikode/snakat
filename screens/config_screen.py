from screens.screen import Button, Screen
from config import CATS, CONFIG_SCREEN, FOODS, GAME_SCREEN, SIZES, SPEED, is_clicked
import pygame


class ConfigScreen(Screen):
    cube_color = (234, 12, 139)

    def __init__(self):
        super().__init__(CONFIG_SCREEN, CONFIG_SCREEN)
        self.cube = [200, 100, 800, 500]
        self.set_config_list()

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
        self.update_config_list()

    def get_config_img(self, name):
        return pygame.image.load(
            'imgs/configs/'+str(name)+'_config.png').convert_alpha()

    def set_config_list(self):
        self.list = []
        self.list.append([CATS, 0])
        self.list.append([FOODS, 0])

        sizes = []
        for size in SIZES:
            sizes.append('size_'+str(size))
        self.list.append([sizes, 0])

        speeds = []
        for speed in SPEED:
            speeds.append('speed_'+str(speed))
        self.list.append([speeds, 0])

        self.cat_img = CATS[self.list[0][1]]
        self.food_img = FOODS[self.list[1][1]]
        self.tiles = SIZES[self.list[2][1]]
        self.speed = SPEED[self.list[3][1]]

    def update_config_list(self):
        self.cat_img = CATS[self.list[0][1]]
        self.food_img = FOODS[self.list[1][1]]
        self.tiles = SIZES[self.list[2][1]]
        self.speed = SPEED[self.list[3][1]]

    def draw_row(self, list, index, y):

        if index > 0:
            element_img = self.get_config_img(list[index-1])
            element_img.set_alpha(150)
            self.surface.blit(element_img, (350, y))

        element_img = self.get_config_img(list[index])
        element_img.set_alpha(300)

        self.surface.blit(element_img, (500, y))

        if index < len(list) - 1:
            element_img = self.get_config_img(list[index+1])
            element_img.set_alpha(150)

            self.surface.blit(element_img, (650, y))

    def count(self, row, direction):
        self.list[row][1] += direction

    def draw(self):
        super().draw_frame()
        list_buttons = []

        pygame.display.set_caption("Snakat - Config")
        pygame.draw.rect(self.surface, (12, 242, 9), [
                         0, 0, self.width, self.height])
        self.draw_buttons()

        # lista vertical
        # food
        for (index, row) in enumerate(self.list):
            y = 100 + index * (25+75)
            self.draw_row(row[0], row[1], y)
            if row[1] > 0:
                list_buttons.append(
                    Button("imgs/configs/arrow_left.png", 200, y,
                           160, 75, lambda i: self.count(i, -1), index)
                )

            if row[1] < len(row[0]) - 1:
                list_buttons.append(
                    Button("imgs/configs/arrow_right.png", 840, y,
                           160, 75, lambda i: self.count(i, 1), index)
                )

        # size
        # cat color

        self.buttons = [
            Button("imgs/initial_button_infos.png", 1070, 10, 120,
                   120, lambda: self.change_screen(GAME_SCREEN)),
        ] + list_buttons

        self.surface.blit(self.light, (0, 0))
