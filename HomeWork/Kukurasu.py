from constraint import *


# kukurasu game

def sum_conflict(*args):
    inner_sum = 0
    l1 = args
    for i in range(0, len(l1)):
        if l1[i] == 1:
            inner_sum += i + 1
    return inner_sum


if __name__ == '__main__':
    problem = Problem(RecursiveBacktrackingSolver())
    vars = []
    for i in range(1, 5):
        for j in range(1, 5):
            vars.append((i, j))
    print(vars)
    vars = tuple(vars)
    domains = (0, 1)
    problem.addVariables(vars, domains)
    # constraints
    row_sums = [0, 7, 7, 4, 5]
    col_sums = [0, 3, 4, 10, 3]

    for i in range(1, 5):
        column = []
        for j in range(1, 5):
            column.append((i, j))
        problem.addConstraint(lambda *args: sum_conflict(args) == col_sums[i], column)

    for j in range(1, 5):
        row = []
        for i in range(1, 5):
            row.append((i, j))
        problem.addConstraint(lambda *args: sum_conflict(args) == row_sums[j], row)

    solution = problem.getSolution()
    print(solution)
