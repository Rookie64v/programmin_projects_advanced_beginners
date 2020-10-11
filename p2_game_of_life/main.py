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

    def next_state(self) -> None:
        next_state = self.state.copy()
        for row_idx in range(len(next_state)):
            for col_idx in range(len(next_state[0])):
                alive_neighbours = self._get_alive_neighbours(row_idx, col_idx)
                if alive_neighbours <= 1 or alive_neighbours > 3:
                    next_state[row_idx][col_idx] = 0
                # alive_neighbours == 2 keeps value, that was done by copy()
                elif alive_neighbours == 3:
                    next_state[row_idx][col_idx] = 1
        self.state = next_state

    def _get_alive_neighbours(self, row_idx: int, col_idx: int) -> int:
        alive_neighbours = 0
        for i in (row_idx-1, row_idx, row_idx+1):
            if i < 0 or i >= self.height:
                continue
            for j in (col_idx-1, col_idx, col_idx+1):
                if j < 0 or j >= self.width:
                    continue
                if (i, j) == (row_idx, col_idx):
                    continue
                if self.state[i][j]:
                    alive_neighbours += 1
        return alive_neighbours

    def __str__(self):
        s = ''
        horizontal_border = '--' * len(self.state[0])
        corner = '+'
        vertical_border_bit = '|'
        s += corner + horizontal_border + corner + '\n'
        for row in self.state:
            s += vertical_border_bit
            for bit in row:
                s += f'{"##" if bit else "  "}'
            s += vertical_border_bit + '\n'
        s += corner + horizontal_border + corner + '\n'
        return s


if __name__ == '__main__':
    import time
    board = Board(width=20, height=20)
    board.randomize()
    print(board)
    for i in range(100):
        board.next_state()
        print(board)
        time.sleep(0.3)
