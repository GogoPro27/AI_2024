import random

from searching_framework import *


def check(x, dir):
    if dir == 'down':
        return x < 6
    if dir == 'up':
        return x > 2
    if dir == 'right':
        return x % 3 != 2
    if dir == 'left':
        return x % 3 != 0


class Puzzle(Problem):
    coordinates = {
        0: (0, 2), 1: (1, 2), 2: (2, 2),
        3: (0, 1), 4: (1, 1), 5: (2, 1),
        6: (0, 0), 7: (1, 0), 8: (2, 0)
    }

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}
        star_idx = state.index('*')
        # print(state)

        # u
        curr_state = list(state)
        swap_idx = star_idx - 3
        if check(star_idx, 'up'):
            curr_state[star_idx], curr_state[swap_idx] = curr_state[swap_idx], curr_state[star_idx]
            successors['u'] = tuple(curr_state)
        # d
        curr_state = list(state)
        swap_idx = star_idx + 3
        if check(star_idx, 'down'):
            curr_state[star_idx], curr_state[swap_idx] = curr_state[swap_idx], curr_state[star_idx]
            successors['d'] = tuple(curr_state)
        # l
        curr_state = list(state)
        swap_idx = star_idx - 1
        if check(star_idx, 'left'):
            curr_state[star_idx], curr_state[swap_idx] = curr_state[swap_idx], curr_state[star_idx]
            successors['l'] = tuple(curr_state)
        # r
        curr_state = list(state)
        swap_idx = star_idx + 1
        if check(star_idx, 'right'):
            curr_state[star_idx], curr_state[swap_idx] = curr_state[swap_idx], curr_state[star_idx]
            successors['r'] = tuple(curr_state)
        print(successors,state)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == ('*', 1, 2, 3, 4, 5, 6, 7, 8)

    def h(self, node):
        sum = 0
        for i in range(1, 9):
            num = node.state.index(i)
            x = self.coordinates[num]
            y = self.coordinates[i]
            sum += abs(x[0]-y[0]) + abs(x[1]-y[1])
        return sum


if __name__ == '__main__':
    l1 = ('*', 3, 2, 4, 1, 5, 6, 7, 8)
    # l1 = ['*']
    # while len(l1) != 9:
    #     toPush = random.randint(1, 8)
    #     if toPush not in l1:
    #         l1.append(toPush)

    print(l1)
    l1 = tuple(l1)
    puzzle = Puzzle(l1)

    result_uninformed = breadth_first_graph_search(puzzle)
    print(result_uninformed.solution())

    result_informed = astar_search(puzzle)
    print(result_informed.solution())


