from searching_framework import *


def not_curr(l1, curr):
    if l1[0] != curr:
        return l1[0]
    else:
        return l1[1]


def check(x, y, t1):
    if x == t1[0] and y == t1[1] or x == t1[1] and y == t1[0]:
        return False
    return True


def direction(x, y):
    # 30 31 32 33
    # 20 21 22 23
    # 10 11 12 13
    # 00 01 02 03
    if x[0] < y[0] and x[1] == y[1]:
        return "gore"
    elif x[0] < y[0] and x[1] < y[1]:
        return "gore-desno"
    elif x[0] == y[0] and x[1] < y[1]:
        return "desno"
    elif x[0] > y[0] and x[1] < y[1]:
        return "dole-desno"
    elif x[0] > y[0] and x[1] == y[1]:
        return "dole"
    elif x[0] > y[0] and x[1] > y[1]:
        return "dole-levo"
    elif x[0] == y[0] and x[1] > y[1]:
        return "levo"
    elif x[0] < y[0] and x[1] > y[1]:
        return "gore-levo"


class Explorer(Problem):
    def __init__(self, initial, starting_pos):
        super().__init__(initial, goal=None)
        self.starting_pos = starting_pos
        self.my_dic = {}
        ctr = 1
        for i in range(4):
            for j in range(4):
                self.my_dic[ctr] = (i, j)
                ctr = ctr + 1

    def successor(self, state):
        successors = {}

        curr_pos = state[0]
        paths_left = state[1]
        stars = state[2]

        if curr_pos == -1:
            for s_p in self.starting_pos:
                successors[f"Istrazuvacot pocnuva na poz: {s_p}({self.my_dic[s_p]})"] = (
                    s_p, tuple(paths_left), tuple(stars))
            # print(state, successors)
            return successors

        ways_to_go = [not_curr(l1, curr_pos) for l1 in [x for x in paths_left if curr_pos in x]]

        for way in ways_to_go:
            new_paths_left = [path for path in paths_left if check(way, curr_pos, path)]
            new_pos = way
            new_stars = [star for star in stars if new_pos != star]
            dir = direction(self.my_dic[curr_pos], self.my_dic[new_pos])
            # successors[f"Istrazuvacot se dvizi {dir}"] = (new_pos, tuple(new_paths_left), tuple(new_stars))
            successors[f"Odi {dir}"] = (new_pos, tuple(new_paths_left), tuple(new_stars))

        # print(state, successors)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0

    def h(self, node):  # manhattan
        state = node.state
        if state[0] == -1:
            return 10
        pos = self.my_dic[state[0]]
        value = 0
        if len(state[2]) == 1:
            star = self.my_dic[state[2][0]]
            return abs(pos[0] - star[0]) + abs(pos[1] - star[1])
        elif len(state[2]) == 2:
            star1 = self.my_dic[state[2][0]]
            star2 = self.my_dic[state[2][1]]
            return abs(pos[0] - star1[0]) + abs(pos[1] - star1[1]) + abs(pos[0] - star2[0]) + abs(pos[1] - star2[1])
        else:
            return 0


if __name__ == '__main__':
    initial = (-1, ((1, 2), (1, 5), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (6, 7), (6, 10), (7, 8), (7, 11),
                    (7, 10), (9, 10), (9, 13), (10, 11), (10, 14), (11, 12), (11, 15), (12, 16),
                    (13, 14), (15, 16)), (4, 13))
    starting_positions = (6, 7, 10, 11)
    # print(len(initial))
    explorer = Explorer(initial, starting_positions)
    result_not_informed = breadth_first_graph_search(explorer)
    print(result_not_informed.solution())

    result_informed = astar_search(explorer)
    print(result_informed.solution())
