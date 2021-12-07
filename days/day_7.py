from functools import reduce
from re import findall

memo = {}


def calc_fuel_a(numbers, pos):
    consumed = 0
    for nr in numbers:
        consumed += abs(nr - pos)
    return consumed


def calc_fuel_for_dist(dist):
    return (dist * (dist + 1))/2


def calc_fuel_b(numbers, pos):
    consumed = 0
    for nr in numbers:
        dist = abs(nr - pos)
        if memo.get(dist, None) is None:
            memo[dist] = calc_fuel_for_dist(dist)
        consumed += memo[dist]
    return consumed


def bad_alg_a(numbers):
    start, end = numbers[0], numbers[-1]
    return min([calc_fuel_a(numbers, i) for i in range(start, end + 1)])


def bad_alg_b(numbers):
    start, end = numbers[0], numbers[-1]
    return min([calc_fuel_b(numbers, i) for i in range(start, end + 1)])


###############################################################################
def run_a(input_data):
    numbers = sorted([int(nr) for nr in findall(r'(\d+)', input_data[0])])
    min_fuel = bad_alg_a(numbers)
    return min_fuel


def run_b(input_data):
    numbers = sorted([int(nr) for nr in findall(r'(\d+)', input_data[0])])
    min_fuel = bad_alg_b(numbers)
    return min_fuel
