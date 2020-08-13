import random as r
import src.settings as s


class Grid:

    def __init__(self):
        self.matrix = [[2] * 4 for i in range(4)]

    def __str__(self):
        return "\n".join([str(row) for row in self.matrix])

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def add_rdm_tile(self):
        options = []
        for row in range(4):
            for col in range(4):
                if self.matrix[row][col] == 0:
                    options.append([row, col])

        here = r.choice(options)
        self.matrix[here[0]][here[1]] = r.choices(s.LIST_NUM, s.LIST_PROB)[0]

    def merge(self, row):
        last = [0,0]
        for num in reversed(range(4)):
            if row[num] != last[0] and row[num] != 0:
                last[0] = row[num]
                last[1] = num
            elif row[num] == last[0] and last[0] != 0:
                row[last[1]] *= 2
                row[num] = 0
                last = [0, 0]
        return row

    def move(self, row):
        empty = 0
        for num in reversed(range(4)):
            if row[num] == 0 and num > empty:
                empty = num
            elif row[num] != 0 and empty > num:
                row[empty] = row[num]
                row[num] = 0
                empty -= 1
        return row

    def move_right(self):
        for row in self.matrix:
            self.move(self.merge(row))

    def move_left(self):
        for row in self.matrix:
            row.reverse()
            self.move(self.merge(row))
            row.reverse()

    def move_down(self):
        transposed = [list(row) for row in zip(*self.matrix)]
        for row in transposed:
            self.move(self.merge(row))
        self.matrix = [list(row) for row in zip(*transposed)]


    def move_up(self):
        transposed = [list(row) for row in zip(*self.matrix)]
        for row in transposed:
            row.reverse()
            self.move(self.merge(row))
            row.reverse()
        self.matrix = [list(row) for row in zip(*transposed)]

    def are_moves_available(self):
        transposed = [list(row) for row in zip(*self.matrix)]
        for row in self.matrix:
            if 0 in row:
                return True
            if row != self.merge(row):
                return True
        for col in transposed:
            if col != self.merge(col):
                return True
        return False

