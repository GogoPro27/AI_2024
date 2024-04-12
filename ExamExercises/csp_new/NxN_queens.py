from constraint import *


def get_diagonals(pole, n):
    x, y = pole
    diagonals = []
    while 0 <= x < n and 0 <= y < n:
        diagonals.append((x, y))
        x -= 1
        y += 1
    x, y = pole
    while 0 <= x < n and 0 <= y < n:
        diagonals.append((x, y))
        x -= 1
        y -= 1
    return diagonals


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    n = int(input())
    vars = []
    for i in range(0, n):
        for j in range(0, n):
            vars.append((i, j))

    domains = [0, 1]

    problem.addVariables(tuple(vars), domains)

    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append((i, j))
        problem.addConstraint(ExactSumConstraint(1), row)

    for j in range(0, n):
        col = []
        for i in range(0, n):
            col.append((i, j))
        problem.addConstraint(ExactSumConstraint(1), col)

    for var1 in vars:
        for var2 in vars:
            if var1 == var2:
                continue
            problem.addConstraint(lambda v1, v2: abs(v1[0] - v1[1]) == abs(v2[0] - v2[1]), (var1, var2))

    sol = problem.getSolutions()
    for i in range(0, n):
        for j in range(0, n):
            print(sol[(i, j)], end="\t")
        print()
