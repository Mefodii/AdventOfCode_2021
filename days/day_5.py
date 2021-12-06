import numpy
import collections
from re import match, findall


class Map:

    def __init__(self, width, height, clouds):
        self.width = width
        self.height = height
        self.clouds = clouds
        self.max_overlap = 0
        self.max_overlap_count = 0

        self.mask = numpy.full((width, height), 0)

    def apply_clouds(self, diagonal=False):
        for cloud in self.clouds:
            x1, x2 = min(cloud.x1, cloud.x2), max(cloud.x1, cloud.x2)
            y1, y2 = min(cloud.y1, cloud.y2), max(cloud.y1, cloud.y2)

            if x1 == x2 or y1 == y2:
                self.apply_linear_cloud(x1, x2, y1, y2)
            elif diagonal:
                self.apply_diagonal_cloud(cloud.x1, cloud.x2, cloud.y1, cloud.y2)

    def apply_linear_cloud(self, x1, x2, y1, y2):
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                self.mask[i][j] += 1

    def apply_diagonal_cloud(self, x1, x2, y1, y2):
        dist = abs(x2 - x1) + 1
        x_sign = 1 if x2 > x1 else -1
        y_sign = 1 if y2 > y1 else -1

        for i in range(dist):
            x = x1 + (i * x_sign)
            y = y1 + (i * y_sign)
            self.mask[y][x] += 1

    def calc_max_overlap(self):
        self.max_overlap = max([max(row) for row in self.mask])

    def calc_overlap_count(self):
        for row in self.mask:
            counter = collections.Counter(row)
            for overlap, count in counter.items():
                if overlap >= 2:
                    self.max_overlap_count += count

    def __str__(self):
        result = ""
        for row_nr, row in enumerate(self.mask):
            for col_nr, cell in enumerate(row):
                result += f"{cell} "
            result += "\n"
        return result


class Cloud:

    def __init__(self, data):
        result = findall(r'(\d+)', data)
        self.x1 = int(result[0])
        self.y1 = int(result[1])
        self.x2 = int(result[2])
        self.y2 = int(result[3])

    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"


def build_cloud_map(data: list):
    clouds = [Cloud(line) for line in data]

    max_y, max_x = 0, 0
    for cloud in clouds:
        max_x = max(max_x, cloud.x1, cloud.x2)
        max_y = max(max_y, cloud.y1, cloud.y2)

    _map = Map(max_y + 1, max_x + 1, clouds)

    return _map


###############################################################################
def run_a(input_data):
    _map = build_cloud_map(input_data)
    _map.apply_clouds()
    _map.calc_overlap_count()
    return _map.max_overlap_count


def run_b(input_data):
    _map = build_cloud_map(input_data)
    _map.apply_clouds(diagonal=True)
    _map.calc_overlap_count()
    return _map.max_overlap_count
