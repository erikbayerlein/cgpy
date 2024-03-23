from math import sin
from draw.line.dda.dda import dda


def draw_wave(screen):
    previous_x = 0
    previous_y = 0

    for x in range(1, screen.get_width()-1, 3):
        y = 100*sin(x/16) + screen.get_height()/2

        dda(screen, previous_x, previous_y, x, y, (255, 255, 255))

        previous_x = x
        previous_y = y
