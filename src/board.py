import random as r


class Board:
    def __init__(self):
        self.board = [[0] * 4 for i in range(4)]
        self.score = 0
        self.game_over = False

    def add_rdm_tile(self):
        options = []
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == 0:
                    options.append([row,col])

        here = options[r.randrange(len(options))]
        self.board[here[0]][here[1]] = r.randrange(1,3)

    def move(self, direction):
        pass

    # esto estaría en el loop principal fichando si ya terminó el juego
    def is_game_over(self):
        if self.game_over:
            pass
