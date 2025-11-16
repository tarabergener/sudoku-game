import pygame
import json

from board import SudokuBoard
from draw_board import SudokuUI

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku Game")

# Load JSON board data
with open('board_data.json', 'r') as file:
    easy_board = json.load(file)

# Create board and UI
board = SudokuBoard(easy_board)
ui = SudokuUI(board, screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Get mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            row = (mouse_y - ui.OFFSET) // ui.SQUARE_SIZE
            col = (mouse_x - ui.OFFSET) // ui.SQUARE_SIZE

            if 0 <= row < 9 and 0 <= col < 9:
                ui.select_cell(row, col)

        # Keyboard number input
        if event.type == pygame.KEYDOWN and ui.selected_cell:
            row, col = ui.selected_cell

            if pygame.K_1 <= event.key <= pygame.K_9:
                value = event.key - pygame.K_0
                board.set_cell(row, col, value)

            # Optional: clear cell with Backspace
            elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                board.set_cell(row, col, 0)

            # If R pressed, clear sudoku board
            if event.key == pygame.K_r:
                board.grid = [[0]*9 for _ in range(9)]
            # If D pressed, reset board to default
            if event.key == pygame.K_d:
                default_board = [
                    [5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]
                ]
                board.grid = [row[:] for row in default_board]

    # Draw the grid every frame
    ui.draw_grid()

    # Update the display
    pygame.display.flip()

# End game
pygame.quit()
