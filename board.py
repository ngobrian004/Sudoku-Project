import pygame
from constants import *


class Board:
    def __init__(self, width, height, screen):
        self.rows = 9
        self.cols = 9
        self.width = width
        self.height = height
        self.screen = screen
        self.board = self.initialize_board()

    def draw(self):
        # draw horizontal lines
        font1 = pygame.font.SysFont(None, 75)
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
                if self.board[i][j] != 0:
                    text1 = font1.render(str(self.board[i][j]), 1, (0, 0, 0))
                    self.screen.blit(text1, (j * 720/9 + 25, i * 720/9 + 20))
                
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

    # Checks if the board is full
    def is_full(self):
        if any(0 in sublist for sublist in self.board):
            return False
        else:
            return True

    # Checks if the board is filled correctly
    def check_board(self):
        for i in range(9):
            if len(set(self.board[i])) != 9:
                return False
        for i in range(9):
            col = [item[i] for item in self.board]
            if len(set(col)) != 9:
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                vals = self.board[i][j: j + 3]
                vals.extend(self.board[i + 1][j: j + 3])
                vals.extend(self.board[i + 2][j: j + 3])
            if len(set(vals)) != 9:
                return False
        else:
            return True
