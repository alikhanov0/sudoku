import random
from models.board import Board
from solver.backtracking_solver import BacktrackingSolver
import copy


class Generator:
    def __init__(self):
        self.solver = BacktrackingSolver()

    def generate_full_board(self):
        grid = [[0 for _ in range(9)] for _ in range(9)]
        board = Board(grid)
        self.fill_board(board)
        return board

    def fill_board(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True

        row, col = empty

        numbers = list(range(1, 10))
        random.shuffle(numbers)

        for num in numbers:
            if self.is_valid(board, row, col, num):
                board.set_value(row, col, num)

                if self.fill_board(board):
                    return True

                board.set_value(row, col, 0)

        return False

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board.get_value(i, j) == 0:
                    return (i, j)
        return None

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board.get_value(row, i) == num:
                return False

        for i in range(9):
            if board.get_value(i, col) == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board.get_value(i, j) == num:
                    return False

        return True

    def remove_numbers(self, board, difficulty):
        if difficulty == "easy":
            remove_count = 30
        elif difficulty == "medium":
            remove_count = 40
        else:
            remove_count = 50

        while remove_count > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            if board.get_value(row, col) != 0:
                board.set_value(row, col, 0)
                remove_count -= 1

        return board

    def generate(self, difficulty="easy"):
        full_board = self.generate_full_board()
        puzzle = copy.deepcopy(full_board)
        puzzle = self.remove_numbers(puzzle, difficulty)
        return puzzle