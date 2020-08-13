import random as r
import src.settings as s


class Grid:

    def add_rdm_tile(self, matrix):
        options = []
        for row in range(4):
            for col in range(4):
                if matrix[row][col] == 0:
                    options.append([row, col])

        here = r.choice(options)
        matrix[here[0]][here[1]] = r.choices(s.LIST_NUM, s.LIST_PROB)[0]
        return matrix

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

    def move_right(self, matrix):
        for row in matrix:
            self.move(self.merge(row))
        return matrix

    def move_left(self, matrix):
        for row in matrix:
            row.reverse()
            self.move(self.merge(row))
            row.reverse()
        return matrix

    def move_down(self, matrix):
        transposed = [list(row) for row in zip(*matrix)]
        for row in transposed:
            self.move(self.merge(row))
        matrix = [list(row) for row in zip(*transposed)]
        return matrix

    def move_up(self, matrix):
        transposed = [list(row) for row in zip(*matrix)]
        for row in transposed:
            row.reverse()
            self.move(self.merge(row))
            row.reverse()
        matrix = [list(row) for row in zip(*transposed)]
        return matrix

    def are_moves_available(self, matrix):
        transposed = [list(row) for row in zip(*matrix)]
        for row in matrix:
            if 0 in row:
                return True
            if row != self.merge(row):
                return True
        for col in transposed:
            if col != self.merge(col):
                return True
        return False

