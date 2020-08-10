import random as r

class Grid:

    def __init__(self):
        self.matrix = [[0] * 4 for i in range(4)]


    def add_rdm_tile(self):
        options = []
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == 0:
                    options.append([row ,col])

        here = r.choice(options)
        self.board[here[0]][here[1]] = r.choice([2, 2, 2, 4])


    def move_left(self):
        pass

    def move_right(self):
        pass