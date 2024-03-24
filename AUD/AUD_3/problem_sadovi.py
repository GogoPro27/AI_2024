from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Container(Problem):

    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):
        # (j0,j1)

        successors = {}

        j0, j1 = state
        c0, c1 = self.capacities

        if j0 > 0:
            successors["Isprazni go sadot J0"] = (0, j1)
        if j1 > 0:
            successors["Isprazni go sadot J1"] = (j1, 0)

        if j0 > 0 and j1 < c1:
            delta = min(c1 - j1, j0)
            successors["Preturi od J0 vo J1"] = (j0 - delta, j1 + delta)

        if j1 > 0 and j0 < c0:
            delta = min(c0 - j0, j1)
            successors["Preturi od J1 vo J0"] = (j0 + delta, j1 - delta)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return super().goal_test(state)

    def path_cost(self, c, state1, action, state2):
        return super().path_cost(c, state1, action, state2)

    def value(self):
        pass


if __name__ == '__main__':
    container = Container((15, 5), (5, 5), (0, 0))

    result = breadth_first_graph_search(container)
    print(result.solution())
    print(result.solve())
