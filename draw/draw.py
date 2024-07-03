import pygame
from numpy import pi, cos, sin, arange, floor

from draw.polygon.polygon import Polygon


class Draw:
    def set_pixel(screen, x, y, color):
        if x < 0:
            x = 0
        if y < 0:
            y = 0

        if x >= screen.get_width():
            x = screen.get_width() - 1
        if y >= screen.get_height():
            y = screen.get_height() - 1

        pixel = pygame.Rect((x, y, 1, 1))
        pygame.draw.rect(screen, color, pixel)


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
            Draw.set_pixel(screen, initial_x + x * xx + y * yx, initial_y + x * xy + y * yy, color)

            if p >= 0:
                y += 1
                p -= dx2

            p += dy2


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

        Draw.set_pixel(screen, round(x), round(y), color)

        for _ in range(int(steps)):
            x = x + steps_x
            y = y + steps_y
            Draw.set_pixel(screen, round(x), round(y), color)

    # TO DO: bugando
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

        Draw.set_pixel(screen, int(x), int(y), color)

        for _ in range(1, steps + 1):
            x = x * step_x
            y = y * step_y

            if step_x == 1:
                prop = abs(y - int(y))
                Draw.set_pixel(screen, int(x), int(y), round((1 - prop) * color))
                Draw.set_pixel(screen, int(x), int(y + sign(step_y)), round(prop * color))
            else:
                prop = abs(x - int(x))
                # bugando aqui
                Draw.set_pixel(screen, int(x), int(y), round((1 - prop) * color))
                Draw.set_pixel(screen, int(x), int(y + sign(step_y)), round(prop * color))
    

    def draw_polygon(screen, polygon, color):
        for i in range(len(polygon.points) - 1):
            Draw.dda(screen, polygon.points[i][0], polygon.points[i][1], polygon.points[i + 1][0], polygon.points[i + 1][1], color)

        Draw.dda(screen, polygon.points[len(polygon.points) - 1][0], polygon.points[len(polygon.points) - 1][1], polygon.points[0][0], polygon.points[0][1], color)
    

    def circumference(screen, x_center, y_center, radius, color):
        c = Polygon()

        for angle in arange(0, 2 * pi, 0.25):
            c.insert_vertex(floor(x_center + radius * cos(angle)), floor(y_center + radius * sin(angle)))

        Draw.draw_polygon(screen, c, color)
        



def sign(x):
    if x < 0:
        return -1
    else:
        return 1
