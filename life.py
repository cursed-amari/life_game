import pygame
import random
import sys

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 10

ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

cells = [[random.randint(0, 1) for _ in range(COLS)] for _ in range(ROWS)]


def draw_grid():
    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):
            if cells[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
                )

    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def count_neighbors(row, col):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue

            neighbor_row = (row + dr) % ROWS
            neighbor_col = (col + dc) % COLS
            count += cells[neighbor_row][neighbor_col]
    return count


def update_cells():
    global cells
    new_cells = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLS):
            neighbors = count_neighbors(row, col)

            if cells[row][col] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_cells[row][col] = 1
                else:
                    new_cells[row][col] = 0
            else:
                if neighbors == 3:
                    new_cells[row][col] = 1
                else:
                    new_cells[row][col] = 0

    cells = new_cells


clock = pygame.time.Clock()
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        update_cells()

    draw_grid()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()

