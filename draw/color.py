import time
import pygame

from draw.draw import Draw
import screen.get_pixel as gp


class Color:
    def flood_fill(self, x, y, color, animation=False):
        initial_color = Color(gp.get_pixel(x, y))

        if color == initial_color:
            return

        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            if Color(gp.get_pixel(x, y)) != initial_color:
                continue

            if animation:
                time.sleep(0.000001)
                pygame.display.update()

            Draw.set_pixel(x, y, color)

            if x + 1 < self.width:
                stack.append((x + 1, y))

            if x >= 1:
                stack.append((x - 1, y))

            if y + 1 < self.height:
                stack.append((x, y + 1))

            if y >= 1:
                stack.append((x, y - 1))


    def boundary_fill(self, x, y, color, border_color=None):
        stack = [(x, y)]

        if not border_color:
            border_color = color

        while stack:
            x, y = stack.pop()

            color_aux = Color(gp.get_pixel(x, y))

            if color_aux in [border_color, color]:
                continue

            Draw.set_pixel(x, y, color)

            if x + 1 < self.width:
                stack.append((x + 1, y))

            if x >= 1:
                stack.append((x - 1, y))

            if y + 1 < self.height:
                stack.append((x, y + 1))

            if y >= 1:
                stack.append((x, y - 1))


    def scanline_base(screen, polygon, color):
        y_min = polygon.y_min()
        y_max = polygon.y_max()

        for y in range(y_min, y_max + 1):
            intersections = []

            pix = polygon.points[0][0]
            piy = polygon.points[0][1]

            for p in range(1, len(polygon.points)):
                pfx = polygon.points[p][0]
                pfy = polygon.points[p][1]

                xi = Color.intersection_base(y, [[pix, piy], [pfx, pfy]])

                if xi >= 0:
                    intersections.append(xi)

                pix = pfx
                piy = pfy

            pfx = polygon.points[0][0]
            pfy = polygon.points[0][1]

            xi = Color.intersection_base(y, [[pix, piy], [pfx, pfy]])

            if xi >= 0:
                intersections.append(xi)

            for pi in range(0, len(intersections), 2):
                x1 = intersections[pi]
                x2 = intersections[pi + 1]

                if x2 < x1:
                    x1, x2 = x2, x1

                for xk in range(x1, x2 + 1):
                    Draw.set_pixel(screen, xk, y, color)


    def intersection_base(y, segment):
        xi = segment[0][0]
        yi = segment[0][1]
        xf = segment[1][0]
        yf = segment[1][1]

            # Horizontal segment (has no intersection)
        if yi == yf:
            return -1

            # Secure starting point on top
        if yi > yf:
            xi, xf = xf, xi
            yi, yf = yf, yi

        t = (y - yi) / (yf - yi)

        return int(xi + t * (xf - xi)) if t > 0 and t <= 1 else -1

