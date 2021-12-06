from re import findall

class Fish:
    TIMER_START = 6
    TIMER_NEW = 8

    def __init__(self, timer):
        self.timer = timer

    def lapse(self, time):
        new_fish = None
        self.timer -= 1
        if self.timer == -1:
            new_fish = Fish(self.TIMER_NEW)
            self.timer = self.TIMER_START

        return new_fish

    def __repr__(self):
        return str(self.timer)

    def __str__(self):
        return self.__repr__()


def build_fish(data):
    fishes = [Fish(int(timer)) for timer in findall(r'(\d+)', data[0])]

    for i in range(80):
        new_fishes = []
        for fish in fishes:
            new_fish = fish.lapse(1)
            if new_fish:
                new_fishes.append(new_fish)
        fishes += new_fishes

    return fishes


###############################################################################
def run_a(input_data):
    fishes = build_fish(input_data)
    return len(fishes)


def run_b(input_data):
    return ""
