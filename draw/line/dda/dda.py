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
