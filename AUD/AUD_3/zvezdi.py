from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class StarsProblem(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.rows = 8
        self.cols = 8

    def successor(self, state):
        # state = (x_k,y_k,x_l,y_l,((x1,y1),(x2,y2),(x3,y3)))

        successors = {}

        x_k, y_k = state[0], state[1]
        x_l, y_l = state[2], state[3]

        stars = state[4]

        horse_dic = {(-1, +2): "K1", (+1, +2): "K2",
                     (+2, +1): "K3", (+2, -1): "K4",
                     (+1, -2): "K5", (-1, -2): "K6",
                     (-2, -1): "K7", (-2, +1): "K8"}
        bishop_dic = {(-1, +1): "B1", (+1, +1): "B2",
                      (-1, -1): "B3", (+1, -1): "B4"}

        for key in horse_dic:
            new_x, new_y = key[0] + x_k, key[1] + y_k
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if [new_x, new_y] != [x_l, y_l]:
                    remaining_stars = []
                    for star in stars:
                        if star != (new_x, new_y):
                            remaining_stars.append(star)
                    remaining_stars = tuple(remaining_stars)
                    successors[horse_dic[key]] = (new_x, new_y, x_l, y_l, remaining_stars)

        for key in bishop_dic:
            new_x, new_y = key[0] + x_l, key[1] + y_l
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if [new_x, new_y] != [x_k, y_k]:
                    successors[bishop_dic[key]] = (x_k, y_k, new_x, new_y, tuple([star for star in stars if star != (new_x,new_y)]))

        # print(state, successors)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0


if __name__ == '__main__':
    knight = (2, 5)
    bishop = (5, 1)
    stars_pos = ((1, 1), (4, 3), (6, 6))

    stars = StarsProblem((knight[0], knight[1], bishop[0], bishop[1], stars_pos))

    result = breadth_first_graph_search(stars)
    if result is not None:
        print(result.solution())
