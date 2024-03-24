from searching_framework import *


class Labyrinth(Problem):

    def __init__(self, initial, N, wall_coords, house):
        super().__init__(initial, goal=None)
        self.N = N
        self.wall_coords = wall_coords
        self.house = house
        self.ways_to_go = ((-1, 0), (0, -1), (0, 1), (2, 0), (3, 0))
        self.dirs = ("Levo", "Dolu", "Gore", "Desno 2", "Desno 3")

    def successor(self, state):
        successors = {}
        person = state

        for way, dir in zip(self.ways_to_go, self.dirs):
            if way == (2, 0):
                if (person[0] + 1, person[1]) in self.wall_coords:
                    continue
            if way == (3, 0):
                if (person[0] + 1, person[1]) in self.wall_coords or (person[0] + 2, person[1]) in self.wall_coords:
                    continue
            new_person = (person[0] + way[0], person[1] + way[1])
            if self.valid(new_person):
                successors[dir] = new_person

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.house

    def h(self, node):
        person = node.state
        p_x, p_y = person
        h_x, h_y = self.house
        value = 0

        # ako coveceto e levo od kukjata
        if p_x < h_x:
            distance = h_x - p_x
            if distance == 1:
                return 2
            elif distance % 3 == 0:
                value += distance / 3
            else:
                value += distance // 3 + 1
        # ako coveceto e desno
        if p_x > h_x:
            distance = p_x - h_x
            value += distance
        # ako coveceto e nad
        if p_y > h_y:
            distance = p_y - h_y
            value += distance
        # ako coveceto e pod
        if p_y < h_y:
            distance = h_y - p_y
            value += distance

        return value


    def valid(self, person):
        if not 0 <= person[0] < self.N or not 0 <= person[1] < self.N:
            return False
        return person not in self.wall_coords


if __name__ == '__main__':
    n = int(input())
    num_walls = int(input())
    walls = []
    for i in range(num_walls):
        wall = [int(j) for j in input().split(",")]
        walls.append(tuple(wall))
    person = [int(j) for j in input().split(",")]
    house = [int(j) for j in input().split(",")]
    walls = tuple(walls)
    house = tuple(house)
    person = tuple(person)
    initial_state = person

    problem = Labyrinth(person, n, walls, house)
    # result_uninformed = breadth_first_graph_search(problem)
    # print(result_uninformed.solution())

    result_informed = astar_search(problem)
    if result_informed is None:
        print([])
    else:
        print(result_informed.solution())
