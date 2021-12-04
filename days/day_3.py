
def count_ones(data):
    ones = [0 for _ in range(len(data[0]))]

    for line in data:
        for i, val in enumerate(line):
            ones[i] = ones[i] + int(val)

    return ones


def calc_gamma_rate(ones, size):
    common_threshold = size / 2

    gamma_rate = ""
    for one_count in ones:
        value = "1" if one_count > common_threshold else "0"
        gamma_rate += value

    return gamma_rate


def calc_epsilon_rate(gamma_rate):
    return gamma_rate.replace("0", "2").replace("1", "0").replace("2", "1")


def determine_rating(data: list, index: int, most_common: bool):
    if len(data) == 1:
        return data[0]

    sorted_data = {
        "0": [],
        "1": [],
    }

    [sorted_data[line[index]].append(line) for line in data]

    zeroes = sorted_data["0"]
    ones = sorted_data["1"]

    if most_common:
        new_data = zeroes if len(zeroes) > len(ones) else ones
    else:
        new_data = zeroes if len(zeroes) <= len(ones) else ones

    rating = determine_rating(new_data, index + 1, most_common)
    return rating


def calc_oxygen_generator_rating(data):
    return determine_rating(data, index=0, most_common=True)


def calc_co2_scrubber_rating(data):
    return determine_rating(data, index=0, most_common=False)


###############################################################################
def run_a(input_data):
    ones = count_ones(input_data)
    gamma_rate_bin = calc_gamma_rate(ones, len(input_data))
    epsilon_rate_bin = calc_epsilon_rate(gamma_rate_bin)

    result = int(gamma_rate_bin, 2) * int(epsilon_rate_bin, 2)
    return result


def run_b(input_data):
    oxygen_generator_rating = calc_oxygen_generator_rating(input_data)
    co2_scrubber_rating = calc_co2_scrubber_rating(input_data)
    print(oxygen_generator_rating, co2_scrubber_rating)

    result = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    return result
