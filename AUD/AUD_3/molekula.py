from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def move_left(x_move, y_move, x1, y1, x2, y2, walls):
    while x_move > 0 and [x_move - 1, y_move] not in walls \
           and [x_move - 1, y_move] != [x1, y1] \
           and [x_move - 1, y_move] != [x2, y2]:
        x_move -= 1
    return x_move


def move_right(x_move, y_move, x1, y1, x2, y2, walls):
    while x_move < 8 and [x_move + 1, y_move] not in walls \
           and [x_move + 1, y_move] != [x1, y1] \
           and [x_move + 1, y_move] != [x2, y2]:
        x_move += 1
    return x_move


def move_down(x_move, y_move, x1, y1, x2, y2, walls):
    while y_move > 0 and [x_move, y_move - 1] not in walls \
           and [x_move, y_move - 1] != [x1, y1] \
           and [x_move, y_move - 1] != [x2, y2]:
        y_move -= 1
    return y_move


def move_up(x_move, y_move, x1, y1, x2, y2, walls):
    while (y_move < 6 and [x_move, y_move + 1] not in walls
           and [x_move, y_move + 1] != [x1, y1]
           and [x_move, y_move + 1] != [x2, y2]):
        y_move += 1
    return y_move


class MoleculeProblem(Problem):
    def __init__(self, initial, walls):
        super().__init__(initial)
        self.walls = walls

    def successor(self, state):
        successors = dict()
        # (xl,yl,xo,yo,xd,yd)
        xl, yl = state[0], state[1]
        xo, yo = state[2], state[3]
        xd, yd = state[4], state[5]

        # l
        new_xl = move_left(xl, yl, xo, yo, xd, yd, self.walls)
        if new_xl != xl:
            successors["LeftH1"] = (new_xl, yl, xo, yo, xd, yd)
        new_xl = move_right(xl, yl, xo, yo, xd, yd, self.walls)
        if new_xl != xl:
            successors["RightH1"] = (new_xl, yl, xo, yo, xd, yd)
        new_yl = move_up(xl, yl, xo, yo, xd, yd, self.walls)
        if new_yl != yl:
            successors["UpH1"] = (xl, new_yl, xo, yo, xd, yd)
        new_yl = move_down(xl, yl, xo, yo, xd, yd, self.walls)
        if new_yl != yl:
            successors["DownH1"] = (xl, new_yl, xo, yo, xd, yd)

        # o
        new_xo = move_left(xo, yo, xl, yl, xd, yd, self.walls)
        if new_xo != xo:
            successors["LeftO"] = (xl, yl, new_xo, yo, xd, yd)
        new_xo = move_right(xo, yo, xl, yl, xd, yd, self.walls)
        if new_xo != xo:
            successors["RightO"] = (xl, yl, new_xo, yo, xd, yd)
        new_yo = move_up(xo, yo, xl, yl, xd, yd, self.walls)
        if new_yo != yo:
            successors["Up0"] = (xl, yl, xo, new_yo, xd, yd)
        new_yo = move_down(xo, yo, xl, yl, xd, yd, self.walls)
        if new_yo != yo:
            successors["Down0"] = (xl, yl, xo, new_yo, xd, yd)

        # d
        new_xd = move_left(xd, yd, xo, yo, xl, yl, self.walls)
        if new_xd != xd:
            successors["LeftH2"] = (xl, yl, xo, yo, new_xd, yd)
        new_xd = move_right(xd, yd, xo, yo, xl, yl, self.walls)
        if new_xd != xd:
            successors["RightH2"] = (xl, yl, xo, yo, new_xd, yd)
        new_yd = move_up(xd, yd, xo, yo, xl, yl, self.walls)
        if new_yd != yd:
            successors["UpH2"] = (xl, yl, xo, yo, xd, new_yd)
        new_yd = move_down(xd, yd, xo, yo, xl, yl, self.walls)
        if new_yd != yd:
            successors["DownH2"] = (xl, yl, xo, yo, xd, new_yd)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        if state[1] == state[3] == state[5]:
            return state[0] + 1 == state[2] and state[4] - 1 == state[2]
        return False


if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = MoleculeProblem((h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1]), obstacles_list)
    result = breadth_first_graph_search(molecule)
    print(result.solution())
