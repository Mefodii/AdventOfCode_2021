from utils.classes.Matrix import Matrix

MAX_INT = 99999999999999999999999999


class Cave(Matrix):

    def __init__(self, height, width, init_value=None):
        super().__init__(height, width, init_value)
        self.costs = Matrix(width=self.width, height=self.height, init_value=None)

    def calc_travel_costs(self):
        for y in range(1, self.height):
            for x in range(1, self.width):
                self.costs.set_cell(x, y, self.min_cost(x, y))

    def min_cost(self, x, y):
        up = self.costs.get_cell_or_none(x, y - 1)
        left = self.costs.get_cell_or_none(x - 1, y)

        cell_cost = self.get_cell(x, y)
        if up is None and left is None:
            return cell_cost

        if up is None:
            return left + cell_cost

        if left is None:
            return up + cell_cost

        return min(up + cell_cost, left + cell_cost)


def init_cave(data):
    cave = Cave(height=len(data), width=len(data[0]), init_value=0)
    for y, line in enumerate(data):
        cave.map_row(y, list(map(int, list(line))))

    return cave


###############################################################################
def run_a(input_data):
    cave = init_cave(input_data)
    cave.calc_travel_costs()
    print(cave.costs)
    return ""


def run_b(input_data):
    return ""
