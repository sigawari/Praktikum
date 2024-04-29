import pygame
import random

class SudokuCell:
    def __init__(self, value, row, col, size, font):
        self.value = value
        self.row = row
        self.col = col
        self.size = size
        self.font = font
        self.selected = False

    def draw(self, screen):
        # Draw cell jika tidak kosong
        if self.value != 0:
            text = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.col * self.size + self.size // 2, self.row * self.size + self.size // 2))
            screen.blit(text, text_rect)
        # Untuk higlight
        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (self.col * self.size, self.row * self.size, self.size, self.size), 3)

    def set_value(self, value):
        self.value = value

    def is_selected(self, pos):
        x, y = pos
        return self.row * self.size <= y <= (self.row + 1) * self.size and self.col * self.size <= x <= (self.col + 1) * self.size


class SudokuBoard:
    def __init__(self, grid, size, font):
        self.grid = [[SudokuCell(grid[row][col], row, col, size, font) for col in range(9)] for row in range(9)]

    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)

    def select_cell(self, pos):
        for row in self.grid:
            for cell in row:
                cell.selected = False
                if cell.is_selected(pos):
                    cell.selected = True
                    return cell.row, cell.col
        return None, None

    def set_cell_value(self, row, col, value):
        self.grid[row][col].set_value(value)

class SudokuGame:
    def __init__(self):
        self.grid = self.generate_puzzle()  # Change here
        self.board = SudokuBoard(self.grid, 50, pygame.font.Font(None, 40))
        self.selected_cell = None

    def draw(self, screen):  # Add this method to SudokuGame class
        self.board.draw(screen)
        
    def generate_puzzle(self):  # Updated method
        # Generate a solved Sudoku grid
        solved_grid = [[(i * 3 + i // 3 + j) % 9 + 1 for j in range(9)] for i in range(9)]
        # Shuffle rows
        for _ in range(20):
            row1, row2 = random.randint(0, 8), random.randint(0, 8)
            solved_grid[row1], solved_grid[row2] = solved_grid[row2], solved_grid[row1]
        # Shuffle columns
        for _ in range(20):
            col1, col2 = random.randint(0, 8), random.randint(0, 8)
            for row in solved_grid:
                row[col1], row[col2] = row[col2], row[col1]
        # Remove numbers to create a puzzle
        puzzle_grid = [row[:] for row in solved_grid]
        for _ in range(40):
            row, col = random.randint(0, 8), random.randint(0, 8)
            # Ensure that the generated puzzle remains valid
            while not self.is_valid_move(puzzle_grid, row, col):
                row, col = random.randint(0, 8), random.randint(0, 8)
            puzzle_grid[row][col] = 0
        return puzzle_grid

    def is_valid_move(self, grid, row, col):
        # Check if placing a number at the given position violates Sudoku rules
        num = grid[row][col]
        grid[row][col] = 0
        for i in range(9):
            if grid[i][col] == num or grid[row][i] == num:
                grid[row][col] = num
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    grid[row][col] = num
                    return False
        grid[row][col] = num
        return True

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 450))
    pygame.display.set_caption("Sudoku Game")
    clock = pygame.time.Clock()

    game = SudokuGame()
    running = True

    while running:
        screen.fill((255, 255, 255))
        game.draw(screen)  # Call draw method of SudokuGame
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
