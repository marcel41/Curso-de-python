import numpy as np
class Piece:

    LEFT_MOVEMENT = 0
    RIGHT_MOVEMENT = 1
    DOWN_MOVEMENT = 2

    """Authors: Alexis Jair Rodriguez Nunez
                Marcel Moran Calderon
                """
    def __init__(self, colour, shape, cells, required_cells):
        self.__colour = colour
        self.__shape = shape
        self.__cells = cells

        self.__required_cells = required_cells
        self.update()

    def update(self):
        for cell in self.__required_cells:
            cell.set(self.__colour)

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, cells):
        self.__cells = cells

    @property
    def required_cells(self):
        return self.__required_cells

    @required_cells.setter
    def required_cells(self, required_cells):
        self.__required_cells = required_cells

    def move(self, direction):
        neighbour_cells = []
        neighbour_required_cells = []
        for cell in self.__cells:
            if direction == Piece.LEFT_MOVEMENT:
                neighbour_cell = cell.left
            elif direction == Piece.RIGHT_MOVEMENT:
                neighbour_cell = cell.right
            elif direction == Piece.DOWN_MOVEMENT:
                neighbour_cell = cell.down

            if cell in self.__required_cells:
                # Check it is not one of my own
                if not neighbour_cell.free and neighbour_cell not in self.__required_cells:
                    return False
                else:
                    neighbour_required_cells.append(neighbour_cell)
            neighbour_cells.append(neighbour_cell)

        # Movement is now possible
        # Clear cells
        for cell in self.__required_cells:
            cell.clear()

        # Update references
        self.__required_cells = neighbour_required_cells
        self.__cells = neighbour_cells

        # Colour/update new cells
        self.update()
        return True

    def rotate(self, clockwise):
        positions = np.arange(len(self.__cells)).reshape(self.__shape)
        if clockwise:
            rotated_positions = np.rot90(positions, 3, axes=(0,1))
        else:
            rotated_positions = np.rot90(positions, 1, axes=(0,1))

        rotated_cells = [self.__cells[i] for i in rotated_positions.flatten()]
        required_cells = []
        for cell, rotated_cell in zip(self.__cells, rotated_cells):
            if not cell.free:
                # Check not part of piece
                if rotated_cell not in self.__required_cells and not rotated_cell.free:
                    return False
                else:
                    required_cells.append(rotated_cell)

        for cell in self.__required_cells:
            cell.clear()

        self.__cells = rotated_cells
        self.__required_cells = required_cells

        self.update()
