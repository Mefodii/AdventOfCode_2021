from utils.manipulators import list_to_int


def count_greater(numbers):
    greater_counter = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            greater_counter += 1

    return greater_counter


def three_measurement_combine(numbers):
    combined = []
    for i in range(2, len(numbers)):
        combined.append(numbers[i] + numbers[i - 1] + numbers[i - 2])

    return combined


###############################################################################
def run_a(input_data):
    numbers = list_to_int(input_data)
    greater_counter = count_greater(numbers)
    return greater_counter


def run_b(input_data):
    numbers = list_to_int(input_data)
    combined = three_measurement_combine(numbers)
    greater_counter = count_greater(combined)
    return greater_counter
