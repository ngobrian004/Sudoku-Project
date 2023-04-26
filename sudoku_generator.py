import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


# Defines Sudoku generator class
class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        for i in range(row_length):
            row = []
            for j in range(row_length):
                row.append(0)
            self.board.append(row)
        self.box_length = int(math.sqrt(row_length))

    # Returns board
    def get_board(self):
        return self.board

    # Displays board on console
    def print_board(self):
        for num_row in self.board:
            for num_col in num_row:
                print(num_col, end=" ")
            print()

    # Converts the row into a set and checks if the num is in the set
    def valid_in_row(self, row, num):
        numrow = set(self.board[row])
        if num in numrow:
            return False
        else:
            return True

    # Determines if num is in the specified column
    def valid_in_col(self, col, num):
        for row in range(len(self.board)):
            if self.board[row][col] == num:
                return False
        else:
            return True

    # Determines if num is contained in the 3x3 box specified
    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        else:
            return True

    # Determines if it is valid to enter num at (row, col) in the board
    def is_valid(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        if self.valid_in_col(col, num) and self.valid_in_row(row, num) and self.valid_in_box(row_start, col_start, num):
            return True
        else:
            return False

    # Fills the specified 3x3 box with values
    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                while self.board[i][j] == 0:
                    var = random.randint(1, 9)
                    if self.is_valid(i, j, var):
                        self.board[i][j] = var

    # Fills the three boxes along the main diagonal of the board
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    # Fills the remaining cells of the board
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # Constructs a solution by calling fill_diagonal and fill_remaining
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # Removes the appropriate number of cells from the board
    def remove_cells(self):
        cells = 0
        random_row = random.randint(0, 8)
        random_col = random.randint(0, 8)
        while cells < self.removed_cells:
            if self.board[random_row][random_col] != 0:
                self.board[random_row][random_col] = 0
                random_row = random.randint(0, 8)
                random_col = random.randint(0, 8)
                cells += 1
            else:
                random_row = random.randint(0, 8)
                random_col = random.randint(0, 8)


"""
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
"""


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
