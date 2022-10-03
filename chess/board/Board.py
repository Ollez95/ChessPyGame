import pygame

import sys
sys.path.append('c:\\Users\\Gustavo\\PycharmProjects\\Chess\\util')

from utils import WHITE, GREEN, WIDTH, HEIGHT, MARGIN


class Board:

    def __init__(self) -> None:
        self.grid = []

    def draw_matrix(self):

        # loop for each row
        for row in range(8):
            # for each row, create a list that will
            # represent an entire row
            self.grid.append([])
            for _ in range(8):
                self.grid[row].append(0)

    def draw_grid(self, screen):

        self.draw_matrix()
        for row in range(8):
            for column in range(8):
                color = WHITE
                if self.grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
