import random


class Agent:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.list_moves = []

    def move(self, direction):
        if direction == "l":
            self.x -= 1
        elif direction == 'r':
            self.x += 1
        elif direction == 'd':
            self.y -= 1
        elif direction == 'u':
            self.y += 1
        else:
            print("invalid input")
            return
        self.list_moves.append(direction)

    def print_agent(self):
        print(f"{self.name} is positioned at {self.x}, {self.y}")
        if len(self.list_moves) == 0:
            print(f"    {self.name} hasn't moved yet")
        else:
            s = "   "
            for move in self.list_moves:
                s += move + " "
            print(s)


if __name__ == '__main__':
    agent_list = []
    moves = ['l', 'r', 'u', 'd']

    for i in range(0, 10):
        tmp = Agent(i, i, f"agent{i}")
        agent_list.append(tmp)
        agent_list[i].print_agent()
    print()
    for i in range(0, 10):
        for j in range(0, random.randint(0, 10)):
            random_idx = random.randint(0, len(moves) - 1)
            agent_list[i].move(moves[random_idx])

    for i in range(0, 10):
        agent_list[i].print_agent()
