from types import new_class
from screens.screen import Button, Screen
from config import FONT, GAME_SCREEN, END_GAME_SCREEN, TILES_SIZE, LINE, CURVE, TAIL, HEAD_CURVE, HEAD_UNDER, HEAD, SIZES, PAUSE_SCREEN
import pygame
import random
import time


def where_is(el, prev_el):
    pos_x = 0
    pos_y = 0

    if el[0] < prev_el[0]:
        pos_x = 1
    elif el[0] > prev_el[0]:
        pos_x = -1

    if el[1] < prev_el[1]:
        pos_y = 1
    elif el[1] > prev_el[1]:
        pos_y = -1

    return pos_x, pos_y

pygame.font.init()

class GameScreen(Screen):
    head = (4, 4)
    head_direction = 0
    cat = []
    points = 0
    x = 0
    y = 0
    food = (0, 0)
    animation = 0
    running_animation = False
    game_font = pygame.font.Font(FONT, 20)

    def __init__(self):
        super().__init__(GAME_SCREEN, GAME_SCREEN)
        self.cat_ss = pygame.image.load(
            'imgs/'+self.cat_img+'_spritesheet.png')
        self.tile_imgs = [pygame.image.load(
            'imgs/tile_dark.png'), pygame.image.load('imgs/tile_light.png')]
        self.bg = pygame.image.load('imgs/game_bg.png')
        self.set_random_food()
        self.start_x = (self.width - self.tiles*TILES_SIZE)/2
        self.start_y = (50 + self.height - self.tiles*TILES_SIZE)/2
        self.buttons = [
            Button("imgs/button_pause.png", 1010, 80, 88, 88,
                   lambda: self.change_screen(PAUSE_SCREEN))
        ]
        self.head = (self.tiles/2, self.tiles/2)

    def keyboard_events(self):

        if pygame.key.get_pressed()[pygame.K_LEFT] and self.x != 1:
            self.x = -1
            self.y = 0
        if pygame.key.get_pressed()[pygame.K_UP] and self.y != 1:
            self.x = 0
            self.y = -1

        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.x != -1:
            self.x = 1
            self.y = 0

        if pygame.key.get_pressed()[pygame.K_DOWN] and self.y != -1:
            self.x = 0
            self.y = 1

    def reset(self):
        self.running_animation = False
        self.animation = 0
        self.head = (self.tiles/2, self.tiles/2)
        self.cat = []
        if (self.points > self.high_score):
            self.high_score = self.points
        self.points = 0
        self.set_random_food()

    def game(self):
        if (self.speed == 'slow'):
            speed = 130
        if (self.speed == 'normal'):
            speed = 100
        if (self.speed == 'fast'):
            speed = 30

        if self.tick % speed/2 == 0 and self.animation < 2 and not self.running_animation:
            if self.animation == 0:
                self.animation = 1
            else:
                self.animation = 0
        if self.tick == int(speed/2) * (self.animation-1) and self.running_animation:
            self.animation += 1

        if self.tick >= speed:
            if self.y == -1:
                self.head_direction = 0
            if self.x == -1:
                self.head_direction = 3
            if self.y == 1:
                self.head_direction = 2
            if self.x == 1:
                self.head_direction = 1

            if self.head[0] < 0 or self.head[0] >= self.tiles:
                self.x = 0
            if self.head[1] < 0 or self.head[1] >= self.tiles:
                self.y = 0

            last_head = self.head
            last_pos = last_head

            self.head = (self.head[0] + self.x, self.head[1] + self.y)

            if not self.running_animation and (self.head[0] < 0 or self.head[0] >= self.tiles or self.head[1] < 0 or
                                               self.head[1] >= self.tiles or self.head in self.cat):
                self.head = last_head
                self.running_animation = True
                self.animation = 2
            else:
                if len(self.cat) > 0:
                    last_pos = self.cat[-1]

                    for i in reversed(range(2, len(self.cat))):
                        self.cat[i] = self.cat[i-1]
                    self.cat[0] = self.head
                    self.cat[1] = last_head

            if self.running_animation and self.animation == 4:
                time.sleep(1)
                self.change_screen(END_GAME_SCREEN)
                self.reset()

            if self.head == self.food:
                self.points += 1
                if self.is_win():
                    time.sleep(1)
                    self.change_screen(END_GAME_SCREEN)
                    self.reset()

                if len(self.cat) == 0:
                    self.cat.append(self.head)
                self.cat.append(last_pos)
                self.set_random_food()

            self.tick = 0

    def draw(self):
        self.cat_ss = pygame.image.load(
            'imgs/'+self.cat_img+'_spritesheet.png')
        self.cat_ss = pygame.transform.smoothscale(
            self.cat_ss, (self.cat_ss.get_width()/2, self.cat_ss.get_height()/2))
        pygame.display.set_caption("Snakat - Game: " + str(self.points))
        pygame.draw.rect(self.surface, (214, 164, 103), [
                         0, 0, self.width, self.height])
        self.surface.blit(self.bg, (0, 0))
        self.start_x = (self.width - self.tiles*TILES_SIZE)/2
        self.start_y = (50+self.height - self.tiles*TILES_SIZE)/2

        for i in range(self.tiles):
            for j in range(self.tiles):
                color = (211, 118, 222)
                if j % 2 == i % 2:
                    color = (240, 150, 250)
                pygame.draw.rect(self.surface, color, [
                                 self.start_x + TILES_SIZE * j, self.start_y + TILES_SIZE * i, TILES_SIZE, TILES_SIZE])
                self.surface.blit(self.tile_imgs[int(j % 2 == i % 2)], (self.start_x + TILES_SIZE * j, self.start_y +
                                                                        TILES_SIZE * i))

        for (index, el) in enumerate(self.cat):
            self.move_frag(index, self.animation, self.start_x +
                           TILES_SIZE * el[0], self.start_y + TILES_SIZE * el[1])
        sub_head = self.cat_ss.subsurface(
            (HEAD * TILES_SIZE, self.animation * TILES_SIZE, TILES_SIZE, TILES_SIZE))
        self.surface.blit(pygame.transform.rotate(sub_head, self.head_direction * -90), (self.start_x + TILES_SIZE *
                                                                                         self.head[0], self.start_y +
                                                                                         TILES_SIZE * self.head[1]))
        food_sprite = pygame.image.load(
            'imgs/'+self.food_img+'.png').convert_alpha()
        self.surface.blit(food_sprite, (self.start_x + TILES_SIZE *
                                        self.food[0], self.start_y + TILES_SIZE * self.food[1]))

        score_text = self.game_font.render(f'SCORE: {self.points}', False, (82, 47, 57))
        high_score_text = self.game_font.render(f'HIGH SCORE: {self.high_score}', False, (82, 47, 57))
        self.surface.blit(score_text, (410, 5))
        self.surface.blit(high_score_text, (600, 5))

        self.draw_buttons()

    def set_random_food(self):
        while True:
            rand_x = int(random.random() * self.tiles)
            rand_y = int(random.random() * self.tiles)
            self.food = (rand_x, rand_y)

            if self.head != self.food and self.food not in self.cat:
                break

    def move_frag(self, i, frame, el_x, el_y):
        prev_distance = where_is(self.cat[i], self.cat[i-1])
        if i == 0:
            prev_distance = where_is(self.cat[i+1], self.cat[i])
        direction = 0

        if prev_distance[0] == -1:
            direction = 1

        if prev_distance[1] == 1:
            direction = 2

        if prev_distance[0] == 1:
            direction = 3

        if i == 0:
            horizontal = False
            vertical = False
            prev_distance = where_is(self.cat[i+1], self.cat[i])
            next_distance = where_is(
                self.cat[i], (self.cat[i][0]+self.x, self. cat[i][1]+self.y))

            if next_distance[0] == prev_distance[0] == 0 or next_distance[1] == prev_distance[1] == 0:
                frag = HEAD_UNDER
            else:
                frag = HEAD_CURVE
                if next_distance[1] == 1:
                    direction = 2
                    if prev_distance[0] == -1:
                        horizontal = True
                if next_distance[1] == -1:
                    direction = 0
                    if prev_distance[0] == 1:
                        horizontal = True

                if prev_distance[1] == 1:
                    direction = 1
                    if next_distance[0] == 1:
                        vertical = True

                if prev_distance[1] == -1:
                    direction = 3
                    if next_distance[0] == -1:
                        vertical = True

                sub = self.cat_ss.subsurface(
                    (frag * TILES_SIZE, frame * TILES_SIZE, TILES_SIZE, TILES_SIZE))
                sub = pygame.transform.flip(sub, horizontal, vertical)
                self.surface.blit(pygame.transform.rotate(
                    sub, direction * 90), (el_x, el_y))
                return

        elif i == len(self.cat) - 1:
            frag = TAIL
        else:
            next_distance = where_is(self.cat[i], self.cat[i+1])

            if next_distance[0] == prev_distance[0] == 0 or next_distance[1] == prev_distance[1] == 0:
                frag = LINE
            else:
                frag = CURVE
                # left and right
                if next_distance[1] == 1 or prev_distance[1] == 1:
                    if next_distance[0] == 1 or prev_distance[0] == 1:
                        direction = 3
                    else:
                        direction = 2
                else:
                    if next_distance[0] == 1 or prev_distance[0] == 1:
                        direction = 0
                    else:
                        direction = 1

        sub = self.cat_ss.subsurface(
            (frag * TILES_SIZE, frame * TILES_SIZE, TILES_SIZE, TILES_SIZE))
        self.surface.blit(pygame.transform.rotate(
            sub, direction * 90), (el_x, el_y))
