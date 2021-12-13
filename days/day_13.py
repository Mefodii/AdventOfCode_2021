from utils.classes.Matrix import Matrix as MatrixTemp
from re import search

FOLD_REGEX = r'.*(y|x)=(\d+)'


class Fold:

    X_AXIS = "x"
    Y_AXIS = "y"

    def __init__(self, axis, along: int):
        self.axis = axis
        self.along = along

    def __repr__(self):
        return f"fold along {self.axis}={self.along}"


class Sheet(MatrixTemp):

    def __init__(self, height, width, init_value=None):
        super().__init__(height, width, init_value)
        self.dots = 0

    def mark_dot(self, x, y):
        self.set_cell(x, y, True)

    def count_dots(self):
        dots = 0
        for row in self.matrix:
            dots += sum(row)

        self.dots = dots

    def fold(self, fold: Fold):
        if fold.axis == Fold.X_AXIS:
            self.fold_vertical(fold.along)
        if fold.axis == Fold.Y_AXIS:
            self.fold_horizontal(fold.along)

    def fold_vertical(self, along_x):
        right_columns = [self.get_column(x) for x in range(along_x + 1, self.width)][::-1]
        left_columns = [self.get_column(x) for x in range(along_x)]

        right_len = len(right_columns)
        left_len = len(left_columns)
        new_width = max(right_len, left_len)
        for x in range(new_width):
            for y in range(self.height):
                left_x = left_len - new_width + x
                right_x = right_len - new_width + x
                left_cell = left_columns[left_x][y] if left_x >= 0 else False
                right_cell = right_columns[right_x][y] if right_x >= 0 else False

                dot = left_cell or right_cell
                self.set_cell(x, y, dot)

        self.width = new_width
        for y, row in enumerate(self.matrix):
            self.matrix[y] = row[:new_width]

    def fold_horizontal(self, along_y):
        rows = self.matrix[along_y + 1:]
        for y, row in enumerate(rows[::-1]):
            for x, dot in enumerate(row):
                if dot:
                    self.set_cell(x, y, dot)

        self.height = along_y
        self.matrix = self.matrix[:self.height]

    def __repr__(self):
        result = ""
        for row in self.matrix:
            result += "".join(["#" if cell else " " for cell in row]) + "\n"
        return result


def init_sheet(data: list):
    width = 0
    height = 0

    dots = []
    for line in data:
        x, y = map(int, line.split(","))
        height = max(height, y)
        width = max(width, x)
        dots.append([x, y])

    width += 1
    height += 1
    sheet = Sheet(height=height, width=width, init_value=False)
    [sheet.mark_dot(dot[0], dot[1]) for dot in dots]

    return sheet


def init_folds(data: list):
    folds = []
    for line in data:
        result = search(FOLD_REGEX, line)
        axis = result.group(1)
        along = int(result.group(2))
        folds.append(Fold(axis, along))

    return folds


def parse_data(data: list):
    delimiter = 0
    for i, line in enumerate(data):
        if len(line) == 0:
            delimiter = i
            break

    return data[:delimiter], data[delimiter + 1:]


###############################################################################
def run_a(input_data):
    sheet_data, folds_data = parse_data(input_data)
    sheet = init_sheet(sheet_data)
    folds = init_folds(folds_data)

    sheet.fold(folds[0])
    sheet.count_dots()

    result = sheet.dots
    return result


def run_b(input_data):
    sheet_data, folds_data = parse_data(input_data)
    sheet = init_sheet(sheet_data)
    folds = init_folds(folds_data)

    for fold in folds:
        sheet.fold(fold)

    return sheet.__repr__()
