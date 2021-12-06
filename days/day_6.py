from re import findall

def spawn(days, memo):
    if memo.get(days, None) is not None:
        return memo[days]

    total_spawned = 1
    for i in range(0, days, 7):
        total_spawned += spawn(days - i - 9, memo)

    memo[days] = total_spawned
    return total_spawned


###############################################################################
def run_a(input_data):
    memo = {0: 1}
    fishes = sum([spawn(80 - int(delay), memo) for delay in findall(r'(\d+)', input_data[0])])
    return fishes


def run_b(input_data):
    memo = {}
    fishes = sum([spawn(256 - int(delay), memo) for delay in findall(r'(\d+)', input_data[0])])
    return fishes
