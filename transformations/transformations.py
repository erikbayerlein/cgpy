import numpy as np

from draw.polygon.polygon import Polygon
from draw.polygon.texture_polygon import TexturePolygon


class Transformations:
    def create_transformation_matrix():
        return np.identity(3)


    def compose_translation(matrix, tx, ty):
        return (
            np.array(
                [
                    [1, 0, tx],
                    [0, 1, ty],
                    [0, 0, 1]
                ]
            )
            @ matrix
        )

    
    def compose_scale(matrix, sx, sy):
        return (
            np.array(
                [
                    [sx, 0, 0],
                    [0, sy, 0],
                    [0, 0, 1]
                ]
            )
            @ matrix
        )


    def compose_rotation(matrix, ang):
        ang = (ang * np.pi)/180

        return np.array(
            [
                [np.cos(ang), -np.sin(ang), 0],
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 1]
            ]
            @ matrix
        )

    #bugando
    def compose_mirroring(matrix):
        return (
            np.array(
                [
                    [-1, 0, 0],
                    [0, -1, 0],
                    [0, 0, 1]
                ]
            )
            @ matrix
        )


    def compose_shear(matrix, cx, cy):
        return (
            np.array(
                [
                    [1, cx, 0],
                    [cy, 1, 0],
                    [0, 0, 1]
                ]
            )
            @ matrix
        )


    def apply_transformation(polygon, matrix):
        points = []

        for i in range(len(polygon.points)):
            pt = polygon.points[i][:2]
            pt.append(1)
            pt = np.transpose(pt)

            transformed_pt = matrix @ pt

            transformed_pt = np.transpose(transformed_pt)
            points.append(transformed_pt[:2].tolist())

            for j in range(2, len(polygon.points[i])):
                points[i].append(polygon.points[i][j])

        if type(polygon) is Polygon:
            return Polygon(points)
        return TexturePolygon(points)

