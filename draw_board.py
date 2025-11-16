import pygame

class SudokuUI:
    def __init__(self, board, screen):
        self.board = board
        self.screen = screen

        # Constants
        self.GRID_SIZE = 9
        self.SCREEN_SIZE = 600
        self.OFFSET = 50
        self.SQUARE_SIZE = (self.SCREEN_SIZE - 2 * self.OFFSET) // self.GRID_SIZE
        self.selected_cell = None

        # Colors
        self.BG_COLOR = ("#A2E8DC")       # blue-green background
        self.SQUARE_COLOR = (200, 200, 200)   # light gray squares
        self.LINE_COLOR = (0, 0, 0)           # black lines
        self.NUM_COLOR = (0, 0, 0)            # black numbers

        # Line widths
        self.THIN_LINE = 1
        self.THICK_LINE = 4

        # Font for numbers
        self.font = pygame.font.SysFont(None, self.SQUARE_SIZE // 2)

    def draw_grid(self):
        # Fill background once per frame
        self.screen.fill(self.BG_COLOR)

        # Draw all 9x9 squares
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                x = self.OFFSET + col * self.SQUARE_SIZE
                y = self.OFFSET + row * self.SQUARE_SIZE
                rect = pygame.Rect(x, y, self.SQUARE_SIZE, self.SQUARE_SIZE)
                pygame.draw.rect(self.screen, self.SQUARE_COLOR, rect)
                pygame.draw.rect(self.screen, self.LINE_COLOR, rect, self.THIN_LINE)

                # Draw numbers
                num = self.board.grid[row][col]
                if num != 0:
                    text = self.font.render(str(num), True, self.NUM_COLOR)
                    # center text
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)

        # Draw thicker 3x3 subgrid lines
        for i in range(self.GRID_SIZE + 1):
            width = self.THICK_LINE if i % 3 == 0 else self.THIN_LINE
            # vertical
            pygame.draw.line(
                self.screen, self.LINE_COLOR,
                (self.OFFSET + i * self.SQUARE_SIZE, self.OFFSET),
                (self.OFFSET + i * self.SQUARE_SIZE, self.OFFSET + self.GRID_SIZE * self.SQUARE_SIZE),
                width
            )
            # horizontal
            pygame.draw.line(
                self.screen, self.LINE_COLOR,
                (self.OFFSET, self.OFFSET + i * self.SQUARE_SIZE),
                (self.OFFSET + self.GRID_SIZE * self.SQUARE_SIZE, self.OFFSET + i * self.SQUARE_SIZE),
                width
            )

        # highlight selected cell
        if self.selected_cell:
            row, col = self.selected_cell
            highlight_rect = pygame.Rect(
                self.OFFSET + col*self.SQUARE_SIZE,
                self.OFFSET + row*self.SQUARE_SIZE,
                self.SQUARE_SIZE,
                self.SQUARE_SIZE
            )
            pygame.draw.rect(self.screen, ("#2FBCBC"), highlight_rect, 3)

    def select_cell(self, row, col):
        self.selected_cell = (row, col)