from numpy import pi, cos, sin, arange, floor

from draw.polygon.polygon import Polygon


def circumference(screen, x_center, y_center, radius, color):
    c = Polygon()

    for angle in arange(0, 2 * pi, 0.25):
        c.insert_vertex(floor(x_center + radius * cos(angle)), floor(y_center + radius * sin(angle)))

    c.draw_polygon(screen, color)
