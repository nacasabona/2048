import random as r

class Grid:

    def __init__(self):
        self.matrix = [[0] * 4 for i in range(4)]

    def __str__(self):
        return "\n".join([str(row) for row in self.matrix])

    def add_rdm_tile(self):
        options = []
        for row in range(4):
            for col in range(4):
                if self.matrix[row][col] == 0:
                    options.append([row ,col])

        here = r.choice(options)
        self.matrix[here[0]][here[1]] = r.choice([2, 2, 2, 2, 4])

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
        pass

    def move_up(self):
        #  M_t = zip(*self.matrix)
        pass

    def move_down(self):
        pass

    def are_moves_available(self):
        pass

       



grid = Grid()

grid.matrix = [[2, 0, 0, 0],[0, 4, 0, 0],[0, 2, 0, 0],[2, 2, 2, 4]]
print(grid)
print("///////")
grid.move_right()
print(grid)




                







