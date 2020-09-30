import random
from typing import *


class Board:
    def __init__(self, width: int, height: int,
                 initial_state: Iterable[Iterable[int]] = None):
        self.width = width
        self.height = height
        if initial_state is not None:
            self.state = initial_state
        else:
            self.state = [[0 for c in range(self.width)]
                          for r in range(self.height)]

    def randomize(self) -> None:
        for row in range(self.height):
            bits_of_row = random.getrandbits(self.width)
            for col in range(self.width):
                self.state[row][col] = bits_of_row & 1
                bits_of_row >>= 1

    def __str__(self):
        s = ''
        for row in self.state:
            for bit in row:
                s += f'{bit} '
            s = s.rstrip()
            s += '\n'
        s = s.rstrip()
        return s


if __name__ == '__main__':
    board = Board(width=10, height=5)
    board.randomize()
    print(board)
