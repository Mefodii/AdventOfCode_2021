class Adjacent:
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"
    UP_RIGHT = "UR"
    UP_LEFT = "UL"
    DOWN_RIGHT = "DR"
    DOWN_LEFT = "DL"

    def __init__(self, direction, x, y, cell_value):
        self.direction = direction
        self.x = x
        self.y = y
        self.cell_value = cell_value

    def __repr__(self):
        return f"{self.direction} {self.x} {self.y} {self.cell_value}"


class Matrix:

    def __init__(self, height, width, init_value=None):
        self.matrix = [Matrix.init_row(width, init_value) for _ in range(height)]
        self.height = height
        self.width = width
        self.init_value = init_value

    def get_adjacent(self, x, y, diagonal=False):
        adjacent = [Adjacent(Adjacent.UP, x, y - 1, self.get_cell_or_none(x, y - 1)),
                    Adjacent(Adjacent.DOWN, x, y + 1, self.get_cell_or_none(x, y + 1)),
                    Adjacent(Adjacent.LEFT, x - 1, y, self.get_cell_or_none(x - 1, y)),
                    Adjacent(Adjacent.RIGHT, x + 1, y, self.get_cell_or_none(x + 1, y))]

        if diagonal:
            adjacent.append(Adjacent(Adjacent.UP_RIGHT, x + 1, y - 1, self.get_cell_or_none(x + 1, y - 1)))
            adjacent.append(Adjacent(Adjacent.UP_LEFT, x - 1, y - 1, self.get_cell_or_none(x - 1, y - 1)))
            adjacent.append(Adjacent(Adjacent.DOWN_RIGHT, x + 1, y + 1, self.get_cell_or_none(x + 1, y + 1)))
            adjacent.append(Adjacent(Adjacent.DOWN_LEFT, x - 1, y + 1, self.get_cell_or_none(x - 1, y + 1)))

        return adjacent

    def get_row(self, y):
        return self.matrix[y]

    def get_column(self, x):
        return [row[x] for row in self.matrix]

    def get_cell(self, x, y):
        return self.matrix[y][x]

    def get_cell_or_none(self, x, y):
        if x >= self.width or x < 0:
            return None
        if y >= self.height or y < 0:
            return None

        return self.matrix[y][x]

    def set_cell(self, x, y, value):
        self.matrix[y][x] = value

    def map_row(self, y, row_data):
        for i in range(len(row_data)):
            self.matrix[y][i] = row_data[i]

    def __repr__(self):
        result = ""
        for row in self.matrix:
            for cell in row:
                result += str(cell)
            result += "\n"
        return result

    @staticmethod
    def init_row(size, init_value=None):
        return [init_value for x in range(size)]
