class Board:
    def __init__(self, grid):
        self.grid = grid

    def print_board(self):
        for row in self.grid:
            print(" ".join(str(num) for num in row))

    def is_empty(self, row, col):
        return self.grid[row][col] == 0

    def set_value(self, row, col, value):
        self.grid[row][col] = value

    def get_value(self, row, col):
        return self.grid[row][col]