
from searching_framework import *


def is_snake_valid(snake, red_apples):
    if len(snake) != len(set(snake)):  # ako ima ist par koordinati znaci si se griznala
        return False
    for coord in snake:
        if coord in red_apples:
            return False
    if 0 <= snake[-1][0] < 10 and 0 <= snake[-1][1] < 10:
        return True
    return False


def move_forward(state):
    snake = state[0]
    snake_dir = state[1]
    green_apples = state[2]
    movements = {'l': (-1, 0), 'r': (+1, 0), 'd': (0, -1), 'u': (0, +1)}

    snake_new_head = (snake[-1][0] + movements[snake_dir][0], snake[-1][1] + movements[snake_dir][1])

    if snake_new_head in green_apples:
        # znaci deka kje go snema toa jabolko
        # isto taka zmijata kje se zgolemi
        new_snake = list(snake)
        new_snake.append(snake_new_head)
        new_snake = tuple(new_snake)
        new_green_apples = [apple for apple in green_apples if apple != snake_new_head]
        new_green_apples = tuple(new_green_apples)
        new_state = (new_snake, snake_dir, new_green_apples)
        return new_state
    else:
        new_snake = list(snake)
        new_snake.append(snake_new_head)
        new_snake.pop(0)
        new_snake = tuple(new_snake)
        new_state = (new_snake, snake_dir, green_apples)
        return new_state


def move_left(state):
    snake = state[0]
    snake_dir = state[1]
    green_apples = state[2]
    movements = {'l': (0, -1), 'r': (0, +1), 'd': (+1, 0), 'u': (-1, 0)}
    new_head_positions = {'l': 'd', 'r': 'u', 'd': 'r', 'u': 'l'}
    new_head_dir = new_head_positions[snake_dir]
    snake_new_head = (snake[-1][0] + movements[snake_dir][0], snake[-1][1] + movements[snake_dir][1])

    if snake_new_head in green_apples:
        # znaci deka kje go snema toa jabolko
        # isto taka zmijata kje se zgolemi
        new_snake = list(snake)
        new_snake.append(snake_new_head)
        new_snake = tuple(new_snake)
        new_green_apples = [apple for apple in green_apples if apple != snake_new_head]
        new_green_apples = tuple(new_green_apples)
        new_state = (new_snake, new_head_dir, new_green_apples)
        return new_state
    else:
        new_snake = list(snake)
        new_snake.append(snake_new_head)
        new_snake.pop(0)
        new_snake = tuple(new_snake)
        new_state = (new_snake, new_head_dir, green_apples)
        return new_state


def move_right(state):
    snake = state[0]
    snake_dir = state[1]
    green_apples = state[2]
    movements = {'l': (0, +1), 'r': (0, -1), 'd': (-1, 0), 'u': (+1, 0)}
    new_head_positions = {'l': 'u', 'r': 'd', 'd': 'l', 'u': 'r'}
    new_head_dir = new_head_positions[snake_dir]
    snake_new_head = (snake[-1][0] + movements[snake_dir][0], snake[-1][1] + movements[snake_dir][1])

    if snake_new_head in green_apples:
        # znaci deka kje go snema toa jabolko
        # isto taka zmijata kje se zgolemi
        new_snake = list(snake)
        new_snake.append(snake_new_head)
        new_snake = tuple(new_snake)
        new_green_apples = [apple for apple in green_apples if apple != snake_new_head]
        new_green_apples = tuple(new_green_apples)
        new_state = (new_snake, new_head_dir, new_green_apples)
        return new_state
    else:
        new_snake = list(snake)
        new_snake.append(snake_new_head)
        new_snake.pop(0)
        new_snake = tuple(new_snake)
        new_state = (new_snake, new_head_dir, green_apples)
        return new_state


class Snake(Problem):
    def __init__(self, initial, red_apples):
        super().__init__(initial, goal=None)
        self.red_apples = red_apples

    def successor(self, state):
        successors = {}
        state1 = move_forward(state)
        state2 = move_right(state)
        state3 = move_left(state)
        if is_snake_valid(state1[0], red_apples):
            successors["ProdolzhiPravo"] = state1
        if is_snake_valid(state2[0], red_apples):
            successors["SvrtiDesno"] = state2
        if is_snake_valid(state3[0], red_apples):
            successors["SvrtiLevo"] = state3
        # print(state, successors)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0


if __name__ == '__main__':
    n = int(input())
    red_apples = []
    green_apples = []
    for i in range(n):
        input_array = [int(num) for num in input().split(",")]
        green_apples.append(tuple(input_array))

    m = int(input())
    for i in range(m):
        input_array = [int(num) for num in input().split(",")]
        red_apples.append(tuple(input_array))

    # print(red_apples)
    # print(green_apples)

    #   l , r, u, d
    initial_state = (((0, 9), (0, 8), (0, 7)), 'd', tuple(green_apples))
    game = Snake(initial_state, red_apples)
    solution = breadth_first_graph_search(game)
    if solution is not None:
        print(solution.solution())
    else:
        print([])
