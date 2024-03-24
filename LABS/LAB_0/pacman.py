import os
import random
os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)
class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, position):
        self.x += position[0]
        self.y += position[1]


class Game:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.dots_left = self.num_of_dots()

    def check_around(self, x, y):
        directions_matrix = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        optional_ways = []

        for d in directions_matrix:
            new_x = x + d[0]
            new_y = y + d[1]
            if 0 <= new_x < self.rows and 0 <= new_y < self.cols and self.matrix[new_x][new_y] != '#':
                optional_ways.append(d)

        if len(optional_ways) == 0:
            return [d for d in directions_matrix if 0 <= x + d[0] < self.rows and 0 <= y + d[1] < self.cols]
        else:
            return optional_ways

    def num_of_dots(self):
        return sum(row.count('.') for row in self.matrix)

    def step_in(self, x, y):
        # print("Checking position:", x, y)  # Debug print statement
        if self.matrix[x][y] == '.':
            self.matrix[x][y] = '#'
            self.dots_left -= 1


class Pacman:
    def __init__(self, game=Game([["#", ".", "."] * 3])):
        self.player = Player(0, 0)
        self.game = game
        self.steps = []

    def play_game(self):
        while self.game.dots_left != 0:
            directions_to_move = self.game.check_around(self.player.x, self.player.y)
            rand_idx = random.randint(0, len(directions_to_move) -1)
            self.player.move(directions_to_move[rand_idx])
            self.game.step_in(self.player.x, self.player.y)
            self.steps.append([self.player.x, self.player.y])

    def __repr__(self):
        str_to_return = ""
        for step in self.steps:
            str_to_return += str(step)+"\n"
        return str_to_return


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(0, n):
        row = input()
        row_to_append = []
        for j in range(0, m):
            row_to_append.append(row[j])
        matrix.append(row_to_append)

    game = Game(matrix)
    if game.num_of_dots() == 0:
        print("Nothing to do here")
    else:
        pacman_game = Pacman(game)
        pacman_game.play_game()
        print(pacman_game)
        print(pacman_game.game.matrix)



