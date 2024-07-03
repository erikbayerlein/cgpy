class Polygon:
    def __init__(self, points=[]):
        self.points = points

    def y_min(self):
        return min(int(row[1]) for row in self.points)

    def y_max(self):
        return max(int(row[1]) for row in self.points)

    def insert_vertex(self, x, y):
        self.points.append([x, y])

