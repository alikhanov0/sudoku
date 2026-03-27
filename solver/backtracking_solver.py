from solver.base_solver import Solver

class BacktrackingSolver(Solver):
    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True

        row, col = empty

        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board.set_value(row, col, num)

                if self.solve(board):
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