import random
from copy import deepcopy


class Board:
    def __init__(self, hight, width, cells):
        self.cells = cells
        self.hight = hight
        self.width = width

    def __repr__(self):
        for i in range(m):
            return (self.cells[i])

    def next_step(self):
        self.cells1 = deepcopy(self.cells)
        for i in range(self.hight):
            for j in range(self.width):
                if (i - 1 < 0):
                    if (j - 1 < 0):
                        if (self.cells[i + 1][j].state + self.cells[i][j + 1].state == 2):
                            self.cells1[i][j].state = 1
                        else:
                            self.cells1[i][j].state = 0
                    elif (j + 1 >= m):
                        if (self.cells[i + 1][j].state + self.cells[i][j- 1].state == 2):
                            self.cells1[i][j].state = 1
                        else:
                            self.cells1[i][j].state = 0
                    else:
                        if 2 <= self.cells[i+ 1][j].state + self.cells[i][j + 1].state + self.cells[i][j - 1].state <= 3:
                            self.cells1[i][j].state = 1
                        else:
                            self.cells1[i][j].state = 0

                elif (i + 1 >= n):
                    if (j - 1 < 0):
                        if (self.cells[i - 1][j].state + self.cells[i][j + 1].state == 2):
                            self.cells1[i][j].state = 1
                        else:
                            self.cells1[i][j].state = 0
                    elif (j + 1 >= m):
                        if (self.cells[i - 1][j].state + self.cells[i][j - 1].state == 2):
                            self.cells1[i][j].state = 1
                        else:
                            self.cells1[i][j].state = 0
                    else:
                        if 2 <= self.cells[i - 1][j].state + self.cells[i][j + 1].state + self.cells[i][j- 1].state <= 3:
                            self.cells1[i][j].state = 1
                        else:
                            self.cells1[i][j].state = 0

                elif (j - 1 < 0 and 1 <= i < n - 1):
                    if 2 <= self.cells[i - 1][j].state + self.cells[i][j + 1].state + self.cells[i + 1][j].state <= 3:
                        self.cells1[i][j].state = 1
                    else:
                        self.cells1[i][j].state = 0
                elif (j + 1 >= m and 1 <= i < n - 1):
                    if 2 <= self.cells[i - 1][j].state + self.cells[i][j - 1].state + self.cells[i + 1][j].state <= 3:
                        self.cells1[i][j].state = 1
                    else:
                        self.cells1[i][j].state = 0
                elif (1 <= i < n - 1 and 1 <= j < m - 1):
                    if 2 <= self.cells[i - 1][j].state + self.cells[i][j- 1].state + self.cells[i+ 1][j].state + self.cells[i][j + 1].state <= 3:
                        self.cells1[i][j].state = 1
                    else:
                        self.cells1[i][j].state = 0
        self.cells = self.cells1


class Cell(Board):
    def __init__(self, row, col, state):
        self.state = state
        self.row = row
        self.col = col

    def __repr__(self):
        return f'{self.state}'

    def is_alive(self, brd):
        if brd[self.row][self.col].state == 1:
            return 'Alive'
        else:
            return 'Dead'


n = random.randint(3, 10)
m = random.randint(3, 10)


bd = []
b1 = Board(n, m, bd)
for i in range(n):
    bd.append([])
    for j in range(m):
        bd[i].append(Cell(i, j, random.randint(0, 1)))


for i in range(n):
    print(*bd[i])

print(bd[random.randint(0, n-1)][random.randint(0, m-1)].is_alive(b1.cells))

b1.next_step()

for i in range(n):
    print(*b1.cells[i])
