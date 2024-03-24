from searching_framework import *


def around_obstacle(obstacle):

    s1 = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            s1.add((obstacle[0] + i, obstacle[1] + j))
    return s1

def in_bounds(x):
    if 0 <= x[0] < 8 and 0 <= x[1] < 6:
        return True
    return False


def check_state(state, obstacles): #((x1,y1),(x2,y2))
    if state[0] in obstacles:
        return False
    if state[1] in around_obstacle(obstacles[0]) or state[1] in around_obstacle(obstacles[1]):
        return False
    if in_bounds(state[0]) and in_bounds(state[1]):
        return True
    else:
        return False


class Football(Problem):
    def __init__(self, initial, obstacles_coord, goal_coord):
        super().__init__(initial, goal=None)
        self.obstacles_coord = obstacles_coord
        self.goal_coord = goal_coord

    def successor(self, state):
        ways_to_go = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
        successors = {}
        actions_on_ways_if_no_ball = (
            "Pomesti coveche gore", "Pomesti coveche gore-desno", "Pomesti coveche desno", "Pomesti coveche dolu-desno",
            "Pomesti coveche dolu")
        actions_on_ways_if_ball = (
            "Turni topka gore", "Turni topka gore-desno", "Turni topka desno", "Turni topka dolu-desno",
            "Turni topka dolu")
        player = state[0]
        ball = state[1]

        for way, actionBall, actionNoBall in zip(ways_to_go, actions_on_ways_if_ball, actions_on_ways_if_no_ball):
            new_coord = (player[0] + way[0], player[1] + way[1])
            if new_coord == ball:
                new_ball = (new_coord[0] + way[0], new_coord[1] + way[1])
                new_state = (new_coord, new_ball)
                if check_state(new_state, self.obstacles_coord):
                    successors[actionBall] = new_state
            else:
                new_state = (new_coord, ball)
                if check_state(new_state, self.obstacles_coord):
                    successors[actionNoBall] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal_coord


if __name__ == '__main__':
    player_coord = [int(num) for num in input().split(",")]
    ball_coord = [int(num) for num in input().split(",")]
    obstacles = ((3, 3), (5, 4))
    goal = ((7, 2), (7, 3))
    # print(player_coord,ball_coord)
    initial_state = (tuple(player_coord), tuple(ball_coord))
    football = Football(initial_state, obstacles, goal)
    result = breadth_first_graph_search(football)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
