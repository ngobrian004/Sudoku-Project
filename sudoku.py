import pygame, sys, copy

import sudoku_generator
from constants import *
from board import Board


def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, BUTTON_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 250))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw game mode select text
    subtitle_surface = start_title_font.render("Select Game Mode:", 0, BUTTON_COLOR)
    subtitle_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(subtitle_surface, subtitle_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(BUTTON_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(BUTTON_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(BUTTON_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 150))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # Should call easy game mode board
                    return 30
                elif medium_rectangle.collidepoint(event.pos):
                    # Should call to generate medium game mode board
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    # Should call to generate hard game mode board
                    return 50
        pygame.display.update()


def redraw():
    # Updates the screen
    screen.fill(BG_COLOR)
    board.draw()
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)


def show_square():
    # Shows what tile is selected
    redraw()
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (clicked_row * DIF - 3, (clicked_col + i) * DIF),
                         (clicked_row * DIF + DIF + 3, (clicked_col + i) * DIF), 7)
        pygame.draw.line(screen, (255, 0, 0), ((clicked_row + i) * DIF, clicked_col * DIF),
                         ((clicked_row + i) * DIF, clicked_col * DIF + DIF), 7)


def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)
    if winner != 0:
        text = 'Game Won!'
    else:
        text = "Game Over :("
    game_over_surf = game_over_font.render(text, 0, BUTTON_COLOR)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)
    restart_surf = game_over_font.render(
        'Press r to play again...', 0, BUTTON_COLOR)
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)

    #  Added key to return to main menu
    menu_surf = game_over_font.render(
        'Press m to return to the main menu...', 0, BUTTON_COLOR)
    menu_rect = menu_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(menu_surf, menu_rect)


if __name__ == '__main__':
    game_over = False
    winner = 0
    val = None
    clicked_col = None
    clicked_row = None

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    difficulty = draw_game_start(screen)  # Calls function to draw start screen

    screen.fill(BG_COLOR)
    # draw_lines()
    # middle_cell = Cell('o', 1, 1, 200, 200)
    # middle_cell.draw(screen)
    board = Board(9, 9, screen, difficulty)
    sudoku = sudoku_generator.generate_sudoku(9, difficulty)
    board.board = copy.deepcopy(sudoku)
    # board.print_board()
    board.draw()

    # Draw "Reset", "Restart", and "Exit" buttons
    # Initialize buttons
    # Initialize text first
    button_font = pygame.font.Font(None, 70)
    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # Initialize button background color and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(BUTTON_COLOR)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 2 - 250, HEIGHT // 2 + 320))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 320))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 + 250, HEIGHT // 2 + 320))

    # Draws the 3 buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if reset_rectangle.collidepoint(mouse_pos):
                    # Should reset the board into initial state
                    board.board = copy.deepcopy(sudoku)
                    redraw()
                    continue
                elif restart_rectangle.collidepoint(mouse_pos):
                    # Should return user to the menu
                    difficulty = draw_game_start(screen)
                    screen.fill(BG_COLOR)
                    board = Board(9, 9, screen, difficulty)
                    sudoku = sudoku_generator.generate_sudoku(9, difficulty)
                    board.board = copy.deepcopy(sudoku)
                    redraw()
                elif exit_rectangle.collidepoint(mouse_pos):
                    # Exits the program
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                clicked_col = int(mouse_pos[1] / SQUARE_SIZE)
                clicked_row = int(mouse_pos[0] / SQUARE_SIZE)
                print(clicked_row, clicked_col)
                if clicked_col < 9:
                    show_square()

            if event.type == pygame.KEYDOWN:
                # Lets you move the cursor with the arrow keys
                if event.key == pygame.K_LEFT and clicked_row is not None and clicked_row != 0:
                    clicked_row -= 1
                    show_square()
                if event.key == pygame.K_RIGHT and clicked_row is not None and clicked_row != 8:
                    clicked_row += 1
                    show_square()
                if event.key == pygame.K_UP and clicked_col is not None and clicked_col != 0:
                    clicked_col -= 1
                    show_square()
                if event.key == pygame.K_DOWN and clicked_col is not None and clicked_col != 8:
                    clicked_col += 1
                    show_square()
                # Chooses what number you want to input with enter
                if event.key == pygame.K_1:
                    val = 1
                if event.key == pygame.K_2:
                    val = 2
                if event.key == pygame.K_3:
                    val = 3
                if event.key == pygame.K_4:
                    val = 4
                if event.key == pygame.K_5:
                    val = 5
                if event.key == pygame.K_6:
                    val = 6
                if event.key == pygame.K_7:
                    val = 7
                if event.key == pygame.K_8:
                    val = 8
                if event.key == pygame.K_9:
                    val = 9
                if event.key == pygame.K_BACKSPACE and sudoku[clicked_col][clicked_row] == 0:
                    # Backspace removes the number from a cell if it was not originally there
                    board.board[clicked_col][clicked_row] = 0
                    board.draw()
                if event.key == pygame.K_RETURN and val is not None and board.board[clicked_col][clicked_row] == 0:
                    # Adds the chosen number to the board if an empty space is selected
                    board.board[clicked_col][clicked_row] = val
                    redraw()
                    if board.is_full() is True:
                        # If the board is full, checks if it is done correctly
                        if board.check_board():
                            winner = 1
                            game_over = True
                        else:
                            winner = 0
                            game_over = True

            # game is over
            if game_over:
                pygame.display.update()
                pygame.time.delay(1000)
                draw_game_over(screen)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        # Should return user to the menu
                        difficulty = draw_game_start(screen)
                        screen.fill(BG_COLOR)
                        board = Board(9, 9, screen, difficulty)
                        sudoku = sudoku_generator.generate_sudoku(9, difficulty)
                        board.board = copy.deepcopy(sudoku)
                        redraw()
                        game_over = False
                    if event.key == pygame.K_r:
                        # Resets the board
                        board.board = copy.deepcopy(sudoku)
                        redraw()
                        game_over = False


            pygame.display.update()
