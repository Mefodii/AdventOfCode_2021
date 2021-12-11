from utils.classes.Matrix import Matrix as MatrixTemplate, Adjacent


class OctopusMap(MatrixTemplate):
    X = "x"
    Y = "y"
    VAL = "val"

    def __init__(self, height, width, init_value=None):
        super().__init__(height, width, init_value)
        self.counter = 0
        self.is_full_light = False

    def init_octopus(self, data):
        for y, row in enumerate(data):
            self.map_row(y, list(map(int, row)))

    def step(self):
        # +1 energy for every octopus
        for y in range(self.height):
            for x in range(self.width):
                self.set_cell(x, y, self.get_cell(x, y) + 1)

        flash_mask = MatrixTemplate(height=self.height, width=self.width, init_value=False)

        flashing = self.get_flashing()
        while len(flashing) > 0:
            flashing = self.flash(flashing, flash_mask)

        count = sum([sum(1 if cell else 0 for cell in row) for row in flash_mask.matrix])
        self.counter += count

        if count == 100:
            self.is_full_light = True

        self.reset_energy()

    def reset_energy(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.get_cell(x, y) > 9:
                    self.set_cell(x, y, 0)

    def flash(self, flashing, flash_mask):
        next_flashing = set([])

        for octopus in flashing:
            y = octopus[0]
            x = octopus[1]
            flash_mask.set_cell(x, y, True)

        for octopus in flashing:
            y = octopus[0]
            x = octopus[1]
            next_flashing = set.union(next_flashing, self.flash_single(x, y, flash_mask))

        return next_flashing

    def flash_single(self, x, y, flash_mask):
        next_flashing = set([])
        adjacent = self.get_adjacent(x, y, diagonal=True)

        for adj in adjacent:
            if adj.cell_value is not None:
                x, y = adj.x, adj.y
                self.set_cell(x, y, self.get_cell(x, y) + 1)
                if self.is_flashing(x, y) and not flash_mask.get_cell(x, y):
                    next_flashing.add((y, x))

        return next_flashing

    def get_flashing(self):
        flashing = []
        for y in range(self.height):
            for x in range(self.width):
                if self.is_flashing(x, y):
                    flashing.append([y, x])

        return flashing

    def is_flashing(self, x, y):
        return self.get_cell(x, y) > 9


def init_map(data):
    height = len(data)
    width = len(data[0])
    octomap = OctopusMap(width=width, height=height, init_value=0)
    octomap.init_octopus(data)

    return octomap


def run_100_steps(octomap):
    for i in range(100):
        octomap.step()


def get_full_light_step(octomap):
    step = 0
    while not octomap.is_full_light:
        octomap.step()
        step += 1

    return step


###############################################################################
def run_a(input_data):
    octomap = init_map(input_data)
    run_100_steps(octomap)
    result = octomap.counter
    return result


def run_b(input_data):
    octomap = init_map(input_data)
    result = get_full_light_step(octomap)
    return result
