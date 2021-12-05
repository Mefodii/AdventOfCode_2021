import numpy, collections
from re import match
from functools import reduce


class Map:

    def __init__(self, width, height, clouds):
        self.width = width
        self.height = height
        self.clouds = clouds
        self.max_overlap = 0
        self.max_overlap_count = 0

        self.mask = numpy.full((width, height), 0)

    def apply_linear_clouds(self):
        for cloud in self.clouds:
            x1, x2 = min(cloud.x1, cloud.x2), max(cloud.x1, cloud.x2)
            y1, y2 = min(cloud.y1, cloud.y2), max(cloud.y1, cloud.y2)

            if x1 != x2 and y1 != y2:
                continue

            for i in range(y1, y2 + 1):
                for j in range(x1, x2 + 1):
                    self.mask[i][j] += 1

    def calc_max_overlap(self):
        self.max_overlap = max([max(row) for row in self.mask])

    def cal_max_overlap_count(self):
        self.max_overlap_count = sum(collections.Counter(row)[self.max_overlap] for row in self.mask)

    def __str__(self):
        result = ""
        for row_nr, row in enumerate(self.mask):
            for col_nr, cell in enumerate(row):
                result += f"{cell} "
            result += "\n"
        return result


class Cloud:

    def __init__(self, data):
        matcher = match(r'(\d+),(\d+).*(\d+),(\d+)', data)
        self.x1 = int(matcher.group(1))
        self.y1 = int(matcher.group(2))
        self.x2 = int(matcher.group(3))
        self.y2 = int(matcher.group(4))

    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"


def build_cloud_map(data: list):
    clouds = [Cloud(line) for line in data]

    max_y, max_x = 0, 0
    for cloud in clouds:
        max_x = max(max_x, cloud.x1, cloud.x2)
        max_y = max(max_y, cloud.y1, cloud.y2)

    _map = Map(max_y + 1, max_x + 1, clouds)
    _map.apply_linear_clouds()
    _map.calc_max_overlap()
    _map.cal_max_overlap_count()

    print(_map.max_overlap, _map.max_overlap_count)
    return _map


###############################################################################
def run_a(input_data):
    _map = build_cloud_map(input_data)
    return ""


def run_b(input_data):
    return ""
