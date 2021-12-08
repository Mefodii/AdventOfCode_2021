from utils.manipulators import subtract_string_list


class Signal:

    def __init__(self, signal, display):
        self.signal = signal
        self.display = display
        self.numbers = {}
        self.segments = {}
        self.number = -1

    def get_signal(self, number):
        for key, value in self.numbers.items():
            if value == number:
                return key
        return ""

    def count_easy_digits(self):
        count = 0
        for digit in self.display:
            on = len(digit)
            if on == 2 or on == 3 or on == 4 or on == 7:
                count += 1
        return count

    def decode(self):
        buffer = {
            5: [],
            6: [],
        }
        numbers = {}
        for digit in self.signal:
            on = len(digit)
            if on == 2:
                self.numbers[digit] = 1
                numbers[1] = list(digit)
            elif on == 3:
                self.numbers[digit] = 7
                numbers[7] = list(digit)
            elif on == 4:
                self.numbers[digit] = 4
                numbers[4] = list(digit)
            elif on == 7:
                self.numbers[digit] = 8
                numbers[8] = list(digit)
            else:
                buffer[on].append(digit)

        # Find number 2
        for digit in buffer.get(5):
            segments = subtract_string_list(numbers[4], list(digit))
            if len(segments) == 2:
                self.numbers[digit] = 2
                numbers[2] = list(digit)
                buffer[5].remove(digit)

        # Find number 9
        for digit in buffer.get(6):
            segments = subtract_string_list(numbers[4], list(digit))
            if len(segments) == 0:
                self.numbers[digit] = 9
                numbers[9] = list(digit)
                buffer[6].remove(digit)

        # Find numbers 5
        for digit in buffer.get(5):
            segments = subtract_string_list(numbers[1], list(digit))
            if len(segments) == 1:
                self.numbers[digit] = 5
                numbers[5] = list(digit)
                buffer[5].remove(digit)

        # Last number in array of 5 digits is 3
        self.numbers[buffer.get(5)[0]] = 3
        numbers[3] = list(buffer.get(5)[0])

        # Find numbers 6
        for digit in buffer.get(6):
            segments = subtract_string_list(numbers[5], list(digit))
            if len(segments) == 0:
                self.numbers[digit] = 6
                numbers[6] = list(digit)
                buffer[6].remove(digit)

        # Last number in array of 6 digits is 0
        self.numbers[buffer.get(6)[0]] = 0
        numbers[0] = list(buffer.get(6)[0])

        self.number = int("".join([str(self.numbers[digit]) for digit in self.display]))

    def __repr__(self):
        return f"{self.signal} {self.display} {self.numbers}"

    def __str__(self):
        return self.__repr__()


def build_signals(data):
    signals = []
    for line in data:
        args = [''.join(sorted(arg)) for arg in line.split(" ")]
        signal = args[:10]
        display = args[11:]
        signals.append(Signal(signal, display))

    return signals


def count_easy_digits(signals):
    return sum(signal.count_easy_digits() for signal in signals)


def decode(signals):
    [signal.decode() for signal in signals]


###############################################################################
def run_a(input_data):
    signals = build_signals(input_data)
    easy_digits = count_easy_digits(signals)
    return easy_digits


def run_b(input_data):
    signals = build_signals(input_data)
    decode(signals)
    result = sum(signal.number for signal in signals)
    return result
