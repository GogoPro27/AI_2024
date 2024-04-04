from searching_framework import *


class Tabla(Problem):

    def __init__(self, initial, green_coords, size):
        super().__init__(initial, goal=None)
        self.columns, self.rows = size  # 5,9
        self.green_cords = green_coords
        self.ways_to_go = [(0, 0), (0, 1), (0, 2), (-1, 1),
                           (-2, 2), (1, 1), (2, 2)]
        self.dirs_to_go = ["Stoj", "Gore 1", "Gore 2",
                           "Gore-levo 1", "Gore-levo 2",
                           "Gore-desno 1", "Gore-desno 2"]

    def successor(self, state):
        successors = {}
        player = state[0]
        home_and_dir = state[1]

        new_home_and_dir = self.move_home(home_and_dir)

        for way, dir in zip(self.ways_to_go, self.dirs_to_go):
            new_player = (player[0] + way[0], player[1] + way[1])
            if new_player in self.green_cords or new_player == new_home_and_dir[0] or new_player == (0, 0):
                new_state = (tuple(new_player), new_home_and_dir)
                successors[dir] = new_state

        # print(state, successors)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1][0]

    def move_home(self, home_and_dir):
        home = home_and_dir[0]
        dir = home_and_dir[1]
        if home[0] == 0:
            dir = 'r'
        elif home[0] == self.columns - 1:
            dir = 'l'
        return ((home[0] + 1, home[1]), dir) if dir == 'r' else ((home[0] - 1, home[1]), dir)

    def h(self, node):
        state = node.state
        player = state[0]
        y_coord = player[1]
        if self.rows - 1 == y_coord:
            return 0
        return (self.rows - 1 - y_coord) / 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    size = (5, 9)
    person_coord = [int(i) for i in input().split(",")]
    house_coord = [int(i) for i in input().split(",")]
    house_dir = "r" if input() == "desno" else "l"

    initial_state = (tuple(person_coord), (tuple(house_coord), house_dir))
    tabla = Tabla(initial_state, allowed, size)

    # result_notInformed = breadth_first_graph_search(tabla)
    # print(result_notInformed.solution())

    result_informed = astar_search(tabla)
    if result_informed is not None:
        print(result_informed.solution())
    else:
        print([])
