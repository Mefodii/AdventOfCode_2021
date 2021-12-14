from collections import Counter


class Polymer:

    def __init__(self, template, insertions):
        self.template = template
        self.insertions = insertions
        self.pairs = Counter(map(str.__add__, template, template[1:]))
        self.count = Counter(template)

    def process(self, steps):
        for step in range(steps):
            new_pairs = self.pairs.copy()
            for (a, b), count in self.pairs.items():
                c = self.insertions[a + b]
                new_pairs[a + c] += count
                new_pairs[c + b] += count
                new_pairs[a + b] -= count
                self.count[c] += count

            self.pairs = new_pairs


def build_insertions(data):
    return dict(line.split(" -> ") for line in data)


def get_min_max_diff(counter):
    return max(counter.values()) - min(counter.values())


###############################################################################
def run_a(input_data):
    template = input_data[0]
    insertions = build_insertions(input_data[2:])
    polymer = Polymer(template, insertions)
    polymer.process(10)
    result = get_min_max_diff(polymer.count)
    return result


def run_b(input_data):
    template = input_data[0]
    insertions = build_insertions(input_data[2:])
    polymer = Polymer(template, insertions)
    polymer.process(40)
    result = get_min_max_diff(polymer.count)
    return result
