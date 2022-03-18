from Contenedor import Contenedor
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_0,
    K_1,
    K_p,
    K_r,
    QUIT,
)

from Pieza import Piece
class Tetris:
    """Authors: Alexis Jair Rodriguez Nunez
                Marcel Moran Calderon
                """
    HORIZONTAL_BOUNDARY_CELLS = 2
    VERTICAL_BOUNDARY_CELLS = 2

    WIDTH = 2*HORIZONTAL_BOUNDARY_CELLS + 10
    HEIGHT = VERTICAL_BOUNDARY_CELLS + 20
    MOVE_DOWN = None
    CELL_SIZE = 30

    def set_up(self):
            self.__screen = pygame.display.set_mode((Tetris.CELL_SIZE*Tetris.WIDTH, Tetris.CELL_SIZE*Tetris.HEIGHT))

            self.__contenedor = Contenedor(Tetris.WIDTH, Tetris.HEIGHT, Tetris.CELL_SIZE)
            # Set borders are not free
            left_border = self.__contenedor.subarea((0, 0), (Tetris.HORIZONTAL_BOUNDARY_CELLS-1, Tetris.HEIGHT-1))
            right_border = self.__contenedor.subarea((Tetris.WIDTH-1-Tetris.HORIZONTAL_BOUNDARY_CELLS+1, 0), (Tetris.WIDTH-1, Tetris.HEIGHT-1))
            bottom_border = self.__contenedor.subarea((0, Tetris.HEIGHT-1-Tetris.VERTICAL_BOUNDARY_CELLS+1), (Tetris.WIDTH-1, Tetris.HEIGHT-1))
            borders = left_border + right_border + bottom_border

            # Mark as not free
            for cell in borders:
                cell.set((0, 0, 255))
                cell.visible = False

            self.create_events()
            self.clock = pygame.time.Clock()
            self.game_over = False
            self.pausado = False
            self.exit = False

            # Create first piece
            self.__contenedor.spawn_piece()

    def start(self):
        self.set_up()
        self.loop()

    def create_events(self):
        Tetris.MOVE_DOWN = pygame.USEREVENT + 1
        FALLING_SPEED_SEC = 1
        pygame.time.set_timer(Tetris.MOVE_DOWN, FALLING_SPEED_SEC*1000)

    def loop(self):
        while not self.exit:
            self.handle_events()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)

    def render(self):
        self.__contenedor.render(self.__screen)

    def handle_events(self):
        events = pygame.event.get()

        # Aqui deberias hacer el manejo de todos aquellos eventos que deberian
        # ser manejados todo el tiempo
            # Reiniciar el juego
                #  usando la tecla R

            # Salir del juego
                # Cuando el usuario presiona la 'X' en la esquina del juego

        if self.game_over or self.pausado:
            return

        # Aqui deberias hacer el manejo de aquellos eventos que solo nos interesan cuando el juego esta corriendo
        for event in events:
            if event.type == KEYDOWN:
                pass

                # Aqui deberias usar las funciones dentro de la clase pieza para permitir las siguientes acciones:
                    # Movimiento a la izquierda:
                    #     Flecha izquierda
                    # Movimiento a la derecha:
                        # Flecha derecha
                    # Rotacion de la pieza sentido horario
                        # Tecla 0
                    # Rotacion de la piexa sentido antihorario
                        # Tecla 1
                    # Enviar la pieza hasta el fondo
                        # Flecha hacia abajo

            elif event.type == Tetris.MOVE_DOWN and not self.pausado:
                if not self.__contenedor.piece.move(Piece.DOWN_MOVEMENT):
                    # Check if row is complete
                    # Get the rows being used by piece
                    rows = {cell.position[1] for cell in self.__contenedor.piece.required_cells}
                    # Get row by row
                    any_row_completed = False
                    for row in rows:
                        row_completed = True
                        row_cells = self.__contenedor.subarea((Tetris.HORIZONTAL_BOUNDARY_CELLS, row), (self.__contenedor.width-1-Tetris.HORIZONTAL_BOUNDARY_CELLS, row))
                        for cell in row_cells:
                            if cell.free:
                                row_completed = False
                                break
                        # if complete clear
                        if row_completed:
                            any_row_completed = True
                            for cell in row_cells:
                                cell.clear()
                    # Push all cells down
                    if any_row_completed:
                        self.__contenedor.shift_cells_down()

                    if not self.__contenedor.spawn_piece():
                        self.game_over = True


if __name__ == '__main__':
    tetris = Tetris()
    tetris.start()