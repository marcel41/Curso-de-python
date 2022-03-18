import pygame
from Celda import Cell
from Pieza import Piece
import numpy as np
import random
class Contenedor:
    """Authors: Alexis Jair Rodriguez Nunez
                Marcel Moran Calderon
                """
  # Width , height are for the visible part of the game
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cells =[[None for x in range(self.width)] for y in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x] = Cell((x, y), cell_size, True)

        for y in range(0, self.height):
            for x in range(0, self.width):
                if y >= 1:
                    self.cells[y][x].up = self.cells[y-1][x]
                if y <= self.height-2:
                    self.cells[y][x].down = self.cells[y+1][x]
                if x >= 1:
                    self.cells[y][x].left = self.cells[y][x-1]
                if x <= self.width-2:
                    self.cells[y][x].right = self.cells[y][x+1]

        # Instantiate the tetris pieces
        self.O_shape = np.array([[0, 0, 0, 0],
                   [0, 1, 1, 0],
                   [0, 1, 1, 0],
                   [0, 0, 0, 0]])

        self.I_shape = np.array([[0, 0, 0, 0],
                   [1, 1, 1, 1],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]])

        self.J_shape = np.array([[1, 0, 0],
                   [1, 1, 1],
                   [0, 0, 0]])

        self.L_shape = np.array([[0, 0, 1],
                   [1, 1, 1],
                   [0, 0, 0]])

        self.S_shape = np.array([[0, 1, 1],
                   [1, 1, 0],
                   [0, 0, 0]])

        self.T_shape = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 0, 0]])

        self.Z_shape = np.array([[1, 1, 0],
                   [0, 1, 1],
                   [0, 0, 0]])

        cyan = (0, 255, 255)
        yellow = (255, 255, 0)
        purple = (148, 0, 211)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        red = (255, 0, 0)
        orange = (255, 215, 0)
        self.shapes_colours = [(self.O_shape, yellow), (self.I_shape, cyan), (self.J_shape, blue), (self.L_shape, orange), (self.S_shape, green), (self.T_shape, purple), (self.Z_shape, red)]
        self.colours = [()]
        self.spawn_x = self.width // 2
        self.spawn_y = 2

    # Set the cell references
    def render(self, screen):
        for h in range(self.height):
            for w in range(self.width):
              if self.cells[h][w].visible :
                  pygame.draw.rect(screen, self.cells[h][w].colour, self.cells[h][w])
                  pygame.draw.rect(screen, (0, 255, 0), self.cells[h][w],1) #border

    def spawn_piece(self):
        # Choose shape to instantiate
        selected_shape, selected_colour = random.choice(self.shapes_colours)

        # Check cells are available
        start_x = self.spawn_x - selected_shape.shape[1]//2
        start_y = self.spawn_y
        spawning_area_cells = [cell for row in self.cells[start_y:start_y+selected_shape.shape[0]] for cell in row[start_x:start_x+selected_shape.shape[1]]]
        required_cells = []
        for cell, required in zip(spawning_area_cells, selected_shape.flatten()):
            if required:
                if not cell.free:
                    return False
                else:
                    required_cells.append(cell)
        self.__piece = Piece(selected_colour, selected_shape.shape, spawning_area_cells, required_cells)
        return True

    @property
    def piece(self):
        return self.__piece

    # Start and end are included in area
    def subarea(self, start, end):
        subarea = []
        start_x, start_y = start
        end_x, end_y = end
        for y in range(start_y, end_y+1):
            for x in range(start_x, end_x+1):
                subarea.append(self.cells[y][x])
        return subarea

    def shift_cells_down(self):
        for y in range(self.height-1, -1, -1):
            for x in range(0, self.width):
                cell = self.cells[y][x]
                # Try to send it to the bottom (until there is no more)
                while True:
                    if not cell.free and cell.down is not None and cell.down.free:
                        cell.down.set(cell.colour)
                        cell.clear()
                        cell = cell.down
                    else:
                        break