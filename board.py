class SudokuBoard:
    def __init__(board, grid):
        board.grid = [row[:] for row in grid]

    def set_cell(board, row, col, value):
        if board.is_valid_move(row, col, value):
            board.grid[row][col] = value

    def get_cell(board, row, col):
        return board.grid[row][col]

    def is_valid_move(board, row, col, num):
        # Check row
        if num in board.grid[row]:
            return False
        # Check col
        for r in range(9):
            if board.grid[r][col] == num:
                return False
        # Check 3x3 square
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board.grid[r][c] == num:
                    return False
        return True
    
    def is_complete(board):
        return all(all(cell != 0 for cell in row) for row in board.grid)