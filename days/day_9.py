from utils.classes.Matrix import Matrix as MatrixTemplate, Adjacent


class Matrix(MatrixTemplate):
    LP_VAL = "lp_val"
    LP = "lp"
    BASIN_SIZE = "basin_size"
    X = "x"
    Y = "y"

    def __init__(self, height, width, init_value=None):
        super().__init__(height, width, init_value)
        self.low_points = []
        self.basins = []

    def find_low_points(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.is_low_point(x, y):
                    self.low_points.append({
                        "x": x,
                        "y": y,
                        Matrix.LP_VAL: self.get_cell_or_none(x, y)
                    })

    def is_low_point(self, x, y):
        current_value = self.get_cell_or_none(x, y)
        adjacent = self.get_adjacent(x, y)
        adjacent_values = [adj.cell_value for adj in adjacent if adj.cell_value is not None]
        min_adjacent = min(adjacent_values)

        return current_value < min_adjacent

    def calc_basins(self):
        for low_point in self.low_points:
            self.basins.append({
                Matrix.LP: low_point,
                Matrix.BASIN_SIZE: self.calc_basin_size(low_point)
            })

    def calc_basin_size(self, low_point):
        basin_mask = MatrixTemplate(self.height, self.width, init_value=0)

        self.build_basin_cells(low_point[Matrix.X], low_point[Matrix.Y], basin_mask)

        basin_size = 0
        for mask_row in basin_mask.matrix:
            basin_size += sum(mask_row)

        print(repr(basin_mask))
        return basin_size

    def build_basin_cells(self, x, y, basin_mask):
        basin_mask.matrix[y][x] = 1

        adjacent = self.get_adjacent(x, y)
        for adj in adjacent:
            if adj.cell_value is not None and adj.cell_value != 9:
                if not basin_mask.matrix[adj.y][adj.x]:
                    self.build_basin_cells(adj.x, adj.y, basin_mask)


def init_matrix(data):
    height = len(data)
    width = len(data[0])

    matrix = Matrix(height, width)
    for i, row in enumerate(data):
        numbers = list(map(int, list(row)))
        matrix.map_row(i, numbers)

    return matrix


###############################################################################
def run_a(input_data):
    matrix = init_matrix(input_data)
    matrix.find_low_points()
    result = sum(low_point[Matrix.LP_VAL] + 1 for low_point in matrix.low_points)

    return result


def run_b(input_data):
    matrix = init_matrix(input_data)
    matrix.find_low_points()
    matrix.calc_basins()
    print(matrix.basins)
    return ""
