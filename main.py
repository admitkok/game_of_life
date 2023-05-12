from copy import deepcopy
from abc import abstractmethod, ABC
from time import sleep
import numpy


class AbstractLifeGameBoard(ABC):
    def __init__(self, width: int = 3, height: int = 3):
        pass

    def __str__(self):
        """Return a string representation of a board.

        Use small o for alive cells and period for empty cells.
        E.g. for board 3x3 with simplest oscillator:
        .o.
        .o.
        .o.
        """
        pass

    @abstractmethod
    def place_cell(self, row: int, col: int):
        """Make a cell alive."""
        pass

    @abstractmethod
    def toggle_cell(self, row: int, col: int) -> None:
        """Invert state of the cell."""
        pass

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def is_alive(self, row: int, col: int) -> bool:
        pass


class Board(AbstractLifeGameBoard):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.state = 0
        self.board = []
        for i in range(height):
            self.board.append([])
            for j in range(width):
                self.board[i].append(0)

    def __str__(self):
        bd = ""
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    bd += "."
                elif self.board[i][j] == 1:
                    bd += "o"
            bd += "\n"
        return bd

    def place_cell(self, row: int, col: int):
        self.board[row][col] = 1

    def toggle_cell(self, row: int, col: int) -> None:
        if self.board[row][col] == 1:
            self.board[row][col] = 0
        elif self.board[row][col] == 0:
            self.board[row][col] = 1

    def is_alive(self, row: int, col: int) -> bool:
        if self.board[row][col] == 1:
            return True
        else:
            return False

    def will_be_alive(self, bd: list[list[int]], row: int, col: int):
        height = self.height
        width = self.width
        nb = 0
        if 1 <= row < height - 1 and 1 <= col < width - 1:
            neighbors = [
                bd[row + dr][col + cr] for dr in (-1, 0, +1) for cr in (-1, 0, +1)
            ]
            nb = numpy.sum(neighbors) - bd[row][col]

        elif 1 <= row < height - 1 and col == 0:
            neighbors = [bd[row + dr][col + cr] for dr in (-1, 0, +1) for cr in (0, +1)]
            nb = numpy.sum(neighbors) - bd[row][col]

        elif 1 <= row < height - 1 and col == width - 1:
            neighbors = [bd[row + dr][col + cr] for dr in (-1, 0, +1) for cr in (-1, 0)]
            nb = numpy.sum(neighbors) - bd[row][col]

        elif row == 0 and 1 <= col < width - 1:
            neighbors = [bd[row + dr][col + cr] for dr in (0, +1) for cr in (-1, 0, +1)]
            nb = numpy.sum(neighbors) - bd[row][col]

        elif row == height - 1 and 1 <= col < width - 1:
            neighbors = [bd[row + dr][col + cr] for dr in (-1, 0) for cr in (-1, 0, +1)]
            nb = numpy.sum(neighbors) - bd[row][col]

        elif row == 0 and col == 0:
            neighbors = [bd[row + dr][col + cr] for dr in (0, +1) for cr in (0, +1)]
            nb = numpy.sum(neighbors) - bd[row][col]

        elif row == height - 1 and col == width - 1:
            neighbors = [bd[row + dr][col + cr] for dr in (-1, 0) for cr in (-1, 0)]
            nb = numpy.sum(neighbors) - bd[row][col]

        elif row == 0 and col == width - 1:
            neighbors = [bd[row + dr][col + cr] for dr in (0, +1) for cr in (-1, 0)]
            nb = numpy.sum(neighbors) - bd[row][col]

        elif row == height - 1 and col == 0:
            neighbors = [bd[row + dr][col + cr] for dr in (-1, 0) for cr in (0, +1)]
            nb = numpy.sum(neighbors) - bd[row][col]

        if nb == 2 and bd[row][col] == 1:
            return True
        elif nb == 3 and bd[row][col] == 0:
            return True
        elif nb == 3 and bd[row][col] == 1:
            return True
        else:
            return False

    def next(self) -> None:
        bd1 = deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                if self.will_be_alive(bd1, i, j) is True:
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0
        self.state += 1


c = CELL_SYMBOL = "o"


if __name__ == "__main__":
    board1 = Board(3, 3)
    for i in range(3):
        board1.place_cell(1, i)

    for i in range(100):
        print(board1)
        board1.next()
        sleep(0.5)
