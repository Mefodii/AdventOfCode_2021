from math import floor


CORRUPTED_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

MATCHING_CLOSE = {
        "(": ")",
        "{": "}",
        "[": "]",
        "<": ">",
}

OPEN_PAR = "({[<"


def is_corrupted(data):
    expected_close = []
    for char in data:
        if char in OPEN_PAR:
            expected_close.append(MATCHING_CLOSE.get(char))
        else:
            if expected_close[-1] == char:
                del expected_close[-1]
            else:
                return char, None

    return None, "".join(expected_close[::-1])


def parse_data(data):
    incomplete = []
    corrupted_chars = ""
    for line in data:
        corrupted, expected_close = is_corrupted(line)
        if corrupted:
            corrupted_chars += corrupted
        else:
            incomplete.append(expected_close)

    return corrupted_chars, incomplete


def calc_middle_score(incomplete):
    scores = []
    for chars in incomplete:
        scores.append(calc_score(chars))

    scores = sorted(scores)
    return scores[floor(len(scores) / 2)]


def calc_score(chars):
    score = 0
    for char in chars:
        score = score * 5 + INCOMPLETE_POINTS[char]

    return score


###############################################################################
def run_a(input_data):
    corrupted_chars, incomplete = parse_data(input_data)
    result = sum(CORRUPTED_POINTS[char] for char in corrupted_chars)
    return result


def run_b(input_data):
    corrupted_chars, incomplete = parse_data(input_data)
    result = calc_middle_score(incomplete)
    return result
