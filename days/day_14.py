from collections import Counter
from math import floor


class Polymer:

    def __init__(self, template, insertions):
        self.template = template
        self.polymer = template
        self.insertions = insertions

    def __repr__(self):
        return f"{self.polymer} {self.insertions}"

    def process(self, steps):
        for step in range(steps):
            half = floor(len(self.polymer)/2)
            self.polymer = self.insert(self.polymer[:half], self.polymer[half:])
            # new_polymer = self.polymer[0]
            # for i, c2 in enumerate(self.polymer[1:]):
            #     c1 = self.polymer[i]
            #     new_c = self.insertions.get(c1 + c2, "")
            #     new_polymer += new_c + c2

            # self.polymer = new_polymer

    def insert(self, left, right):
        insertion = self.insertions.get(left + right, None)
        if not insertion:
            mid_insertion = self.insertions[left[-1] + right[0]]

            left_half = floor(len(left) / 2)
            left_insertion = self.insert(left[:left_half], left[left_half:])

            right_half = floor(len(right) / 2)
            right_insertion = self.insert(right[:right_half], right[right_half:])

            new_insertion = left_insertion[1:] + mid_insertion + right_insertion[:-1]
            self.insertions[left + right] = new_insertion

        return left[0] + self.insertions[left + right] + right[0]


def build_insertions(data):
    insertions = {}
    for line in data:
        pair, elem = line.split(" -> ")
        insertions[pair] = elem

    return insertions


def get_min_max_diff(polymer):
    counter = Counter(polymer.polymer)
    min_c = 99999999999999999
    max_c = 0

    for count in counter.values():
        min_c = min(min_c, count)
        max_c = max(max_c, count)

    return max_c - min_c


###############################################################################
def run_a(input_data):
    template = input_data[0]
    insertions = build_insertions(input_data[2:])
    polymer = Polymer(template, insertions)
    polymer.process(10)
    print(polymer.polymer)
    result = get_min_max_diff(polymer)
    return result


def run_b(input_data):
    template = input_data[0]
    insertions = build_insertions(input_data[2:])
    polymer = Polymer(template, insertions)
    # polymer.process(40)
    result = get_min_max_diff(polymer)
    return result
