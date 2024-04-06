from numpy import sign

from draw.set_pixel import set_pixel


def bresenham(screen, initial_x, initial_y, final_x, final_y, color):
    dx = final_x - initial_x
    dy = final_y - initial_y

    x_sign = 1 if dx > 0 else -1
    y_sign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = x_sign, 0, 0, y_sign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, y_sign, x_sign, 0

    dx2 = 2 * dx
    dy2 = 2 * dy

    p = dy2 - dx
    y = 0

    for x in range(dx):
        set_pixel(screen, initial_x + x * xx + y * yx, initial_y + x * xy + y * yy, color)

        if p >= 0:
            y += 1
            p -= dx2

        p += dy2

    # BUGANDO
    # if final_x < initial_x:
    #     initial_x, final_x = final_x, initial_x
    #     initial_y, final_y = final_y, initial_y
    #
    # dx = abs(final_x - initial_x)
    # dy = abs(final_y - initial_y)
    #
    # aux = False
    # if dy > dx:
    #     dx, dy = dy, dx
    #     aux = True
    #
    # y = 0
    #
    # dy2 = 2 * dy
    # dy2dx2 = dy2 - 2 * dx
    # s = sign(final_y - initial_y)
    #
    # p = dx - dy2
    #
    # for x in range(dx):
    #     if p < 0:
    #         p -= dy2dx2
    #         y += 1
    #     else:
    #         p -= dy2
    #
    #     if aux:
    #         set_pixel(screen, initial_x + x, initial_y + s*y, color)
    #     else:
    #         set_pixel(screen, initial_x + y, initial_y + s*x, color)
