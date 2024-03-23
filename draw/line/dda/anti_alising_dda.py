from draw.set_pixel import set_pixel


def anti_alising_dda(screen, initial_x, initial_y, final_x, final_y, color):
    dx = final_x - initial_x
    dy = final_y - initial_y

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    step_x = dx / steps
    step_y = dy / steps

    x = initial_x
    y = initial_y

    set_pixel(screen, int(x), int(y), color)

    for p in range(1, steps + 1):
        x = x * step_x
        y = y * step_y

        if step_x == 1:
            prop = abs(y - int(y))
            set_pixel(screen, int(x), int(y), round((1 - prop) * color))
            set_pixel(screen, int(x), int(y + sign(step_y)), round(prop * color))
        else:
            prop = abs(x - int(x))
            set_pixel(screen, int(x), int(y), round((1 - prop) * color))
            set_pixel(screen, int(x), int(y + sign(step_y)), round(prop * color))


def sign(x):
    if x < 0:
        return -1
    else:
        return 1
