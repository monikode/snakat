SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

INITIAL_SCREEN = 0
CONFIG_SCREEN = 1
GAME_SCREEN = 2
PAUSE_SCREEN = 3
END_GAME_SCREEN = 4

# top, right, bottom, left
HEAD = 0
HEAD_UNDER = 5
HEAD_CURVE = 6
LINE = 1

# top_left, top_right bottom_left bottom_right
CURVE = 2
TAIL = 3

SIZES = [8, 14, 22]
SPEED = ['slow', 'normal', 'fast']
FOODS = [
    'food_1',
    'food_2',
    'food_3',
    'food_4',
]
CATS = ['cat_white',
        'cat_bw', 'cat_black', 'cat_orange']

TILES_SIZE = 32

FONT = 'fonts/Pixeled.ttf'

def is_clicked(click_coord, rect):
    if click_coord[0] < rect[0] or click_coord[0] > rect[0] + rect[2]:
        return False
    if click_coord[1] < rect[1] or click_coord[1] > rect[1] + rect[3]:
        return False
    return True


def merge(ob1, ob2):
    ob1.__dict__.update(ob2.__dict__)
    return ob1
