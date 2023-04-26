import pygame
from constants import *
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.board = self.initialize_board()
        self.cells = [[Cell(self.board[i][j], i, j, self.height//self.rows,
                            self.width//self.cols) for j in range(cols)] for i in range(rows)]

    def draw(self):
        # draw horizontal lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (BOARD_WIDTH, SQUARE_SIZE * i), LINE_WIDTH)

        # draw vertical lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, BOARD_HEIGHT), LINE_WIDTH)
        # draw horizontal box lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, BOX_COLOR, (0, BOX_SIZE * i),
                            (BOARD_WIDTH, BOX_SIZE * i), LINE_WIDTH)
        # draw vertical box lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, BOX_COLOR, (BOX_SIZE * i, 0),
                             (BOX_SIZE * i, BOARD_HEIGHT), LINE_WIDTH)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)
                
    # Intializes board
    def initialize_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append("-")
            board.append(row)
        return board
    
    # Prints board
    def print_board(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                print(self.board[i][j], end=" ")
            print()   
            
    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
