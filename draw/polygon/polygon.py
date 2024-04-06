from draw.line.dda.dda import dda


class Polygon:
    def __init__(self):
        self.polygon = []

    def insert_vertex(self, x, y):
        self.polygon.append([x, y])

    def draw_polygon(self, screen, color):
        for i in range(len(self.polygon) - 1):
            dda(screen, self.polygon[i][0], self.polygon[i][1], self.polygon[i + 1][0], self.polygon[i + 1][1], color)

        dda(screen, self.polygon[len(self.polygon) - 1][0], self.polygon[len(self.polygon) - 1][1], self.polygon[0][0],
            self.polygon[0][1], color)
