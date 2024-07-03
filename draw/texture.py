from PIL import Image
import numpy as np
import os

from draw.draw import Draw
import screen.get_pixel as gp


class Texture:
    def import_texture(img_name):
        cg_dir = os.getcwd()
        return np.asarray(Image.open(os.path.join(cg_dir, "resources", img_name)))

    def scanline_with_texture(screen, polygon, texture):
        y_min = polygon.y_min()
        y_max = polygon.y_max()

        for y in range(y_min, y_max + 1):
            intersections = []

            for p in range(len(polygon.points)):
                pi = polygon.points[p]
                pf = polygon.points[(p + 1) % len(polygon.points)]

                intersection = Texture.intersection_with_texture(y, [pi, pf])

                if intersection[0] >= 0:
                    intersections.append(intersection)

            intersections.sort(key=lambda intersection: intersection[0])

            for pi in range(0, len(intersections), 2):
                p1 = intersections[pi]
                p2 = intersections[pi + 1]

                x1 = p1[0]
                x2 = p2[0]

                if x1 == x2:
                    continue

                if x2 < x1:
                    p1, p2 = p2, p1

                for xk in range(int(p1[0]), int(p2[0]) + 1):
                    pc = (xk - p1[0]) / (p2[0] - p1[0])

                    tx = p1[2] + pc * (p2[2] - p1[2])
                    ty = p1[3] + pc * (p2[3] - p1[3])

                    color = gp.get_pixel_with_texture(texture, tx, ty)

                    Draw.set_pixel(screen, xk, y, color)


    def intersection_with_texture(y, segment):
        pi = segment[0]
        pf = segment[1]

        # Horizontal segment (has no intersection)
        if pi[1] == pf[1]:
            return [-1, 0, 0, 0]

        # Secure starting point on top
        if pi[1] > pf[1]:
            pi, pf = pf, pi

        t = (y - pi[1]) / (pf[1] - pi[1])

        if t > 0 and t <= 1:
            x = pi[0] + t * (pf[0] - pi[0])

            tx = pi[2] + t * (pf[2] - pi[2])
            ty = pi[3] + t * (pf[3] - pi[3])

            return [x, y, tx, ty]

        return [-1, 0, 0, 0]
