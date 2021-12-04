import numpy


class BingoBoard:

    def __init__(self, data):
        self.board = [list(map(int, line.replace("  ", " ").strip().split(" "))) for line in data]
        self.board_mask = numpy.full((5, 5), False, dtype=bool)
        self.columns_check = [0, 0, 0, 0, 0]
        self.rows_check = [0, 0, 0, 0, 0]
        self.is_bingo = False
        self.score = 0
        self.win_number = -1

    def mark_number(self, number):
        for row_nr, row in enumerate(self.board):
            for col_nr, cell in enumerate(row):
                if cell == number:
                    self.board_mask[row_nr][col_nr] = True
                    self.columns_check[col_nr] += 1
                    self.rows_check[row_nr] += 1

        if 5 in self.columns_check or 5 in self.rows_check:
            self.is_bingo = True

    def calc_score(self):
        for row_nr, row in enumerate(self.board):
            for col_nr, cell in enumerate(row):
                self.score += cell if not self.board_mask[row_nr][col_nr] else 0

    def __repr__(self):
        result = ""
        for row_nr, row in enumerate(self.board):
            for col_nr, cell in enumerate(row):
                result += f"{cell} "
            result += "\n"
        return result


def first_bingo(numbers, boards):
    for number in numbers:
        for board in boards:
            board.mark_number(number)
            if board.is_bingo:
                board.calc_score()
                board.win_number = number
                return board


def last_bingo(numbers, boards):
    last_winner = None
    for number in numbers:
        for board in boards:
            if not board.is_bingo:
                board.mark_number(number)
                if board.is_bingo:
                    board.calc_score()
                    board.win_number = number
                    last_winner = board

    return last_winner


###############################################################################
def run_a(input_data):
    numbers = list(map(int, input_data[0].split(",")))
    boards = [BingoBoard(input_data[i:i+5]) for i in range(2, len(input_data), 6)]

    winner = first_bingo(numbers, boards)
    total_score = winner.score * winner.win_number
    return total_score


def run_b(input_data):
    numbers = list(map(int, input_data[0].split(",")))
    boards = [BingoBoard(input_data[i:i+5]) for i in range(2, len(input_data), 6)]

    winner = last_bingo(numbers, boards)
    total_score = winner.score * winner.win_number
    return total_score
