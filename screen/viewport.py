import numpy as np

from transformations.transformations import Transformations


class Viewport:
    def mapping_window(p, window, viewport):
        initial_x_viewport = viewport[0]
        initial_y_viewport = viewport[1]
        final_x_viewport = viewport[2]
        final_y_viewport = viewport[3]

        initial_x_window = window[0]
        initial_y_window = window[1]
        final_x_window = window[2]
        final_y_window = window[3]

        a = (final_x_viewport - initial_x_viewport)/(final_x_window - initial_x_window)
        b = (final_y_viewport - initial_y_viewport)/(final_y_window - initial_y_window)

        matrix = np.array(
            [
                [a, 0, initial_x_viewport - a * initial_x_window],
                [0, b, initial_y_viewport - b * initial_y_window],
                [0, 0, 1],
            ]
        )

        return Transformations.apply_transformation(p, matrix)

