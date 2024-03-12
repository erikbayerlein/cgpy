from math import sin
from draw.set_pixel import set_pixel


def dda(screen, initial_x, initial_y, final_x, final_y, color):
    dx = final_x - initial_x
    dy = final_y - initial_y

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    steps_x = dx/steps
    steps_y = dy/steps

    x = initial_x
    y = initial_y

    set_pixel(screen, round(x), round(y), color)

    for i in range(int(steps)):
        x = x + steps_x
        y = y + steps_y
        set_pixel(screen, round(x), round(y), color)


def draw_wave(screen):
    previous_x = 0
    previous_y = 0

    for x in range(1, screen.get_width()-1, 3):
        y = 100*sin(x/16) + screen.get_height()/2

        dda(screen, previous_x, previous_y, x, y, (255, 255, 255))

        previous_x = x
        previous_y = y
