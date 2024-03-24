import random

from searching_framework import *


def isValid(state):
    zelka, jare, volk, farmer = state
    if zelka == jare:
        if zelka != farmer:
            return False
    if jare == volk:
        if farmer != jare:
            return False
    return True


class Farmer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}
        state = list(state)
        # zelka jare volk farmer
        new_side_dic = {"w": "e", "e": "w"}
        zelka, jare, volk, farmer = state

        if zelka == farmer:
            new_state = (new_side_dic[zelka], jare, volk, new_side_dic[farmer])
            if isValid(new_state):
                successors["Farmer nosi zelka"] = new_state
        if jare == farmer:
            new_state = (zelka, new_side_dic[jare], volk, new_side_dic[farmer])
            if isValid(new_state):
                successors["Farmer nosi jare"] = new_state
        if volk == farmer:
            new_state = (zelka, jare, new_side_dic[volk], new_side_dic[farmer])
            if isValid(new_state):
                successors["Farmer nosi volk"] = new_state

        new_state = (zelka, jare, volk, new_side_dic[farmer])
        if isValid(new_state):
            successors["Farmer nosi Farmer"] = new_state

        # print(successors, state)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == ("w", "w", "w", "w")

    def h(self, node):
        return len([x for x in node.state if x != 'e'])
        # return random.randint(0,110)

if __name__ == '__main__':
    initial_state = ("e", "e", "e", "e")
    farmer = Farmer(initial_state)
    result = breadth_first_graph_search(farmer)
    print(result.solution())

    result_informed = astar_search(farmer)
    print(result_informed.solution())
