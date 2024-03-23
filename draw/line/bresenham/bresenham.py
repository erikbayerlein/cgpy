from draw.set_pixel import set_pixel


def bresenham(screen, initial_x, initial_y, final_x, final_y, color):
    dx = final_x - initial_x
    dy = final_y - initial_y

    y = initial_y

    p = dx - 2*dy

    for x in range(initial_x, final_x):
        if p < 0:
            p = p - 2*dy + 2*dx
            y = y + 1
        else:
            p = p - 2*dy
        set_pixel(screen, x, y, color)
