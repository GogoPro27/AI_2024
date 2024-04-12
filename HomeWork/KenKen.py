from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = 4
    vars = [i for i in range(0, n * n)]
    # print(vars)
    domains = [i for i in range(1, n + 1)]

    problem.addVariables(vars, domains)

    one_minus = [0, 1]
    four_1 = [2]
    four_2 = [12]
    two_times = [3, 7, 6]
    seven_plus = [4, 5]
    two_divided_1 = [8, 9]
    ten_plus = [10, 11, 15]
    two_divided_2 = [14, 13]

    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(i * n + j)
        # print(row)
        problem.addConstraint(AllDifferentConstraint(), row)

    for j in range(0, n):
        column = []
        for i in range(0, n):
            column.append(i * n + j)
        # print(column)
        problem.addConstraint(AllDifferentConstraint(), column)

    problem.addConstraint(lambda a: a == 4, four_1)
    problem.addConstraint(lambda a: a == 4, four_2)
    problem.addConstraint(lambda x, y: abs(x - y) == 1, one_minus)
    problem.addConstraint(lambda x, y, z: x * y * z == 2, two_times)
    problem.addConstraint(lambda x, y: x + y == 7, seven_plus)
    problem.addConstraint(lambda x, y: x / y == 2 or y / x == 2, two_divided_1)
    problem.addConstraint(lambda x, y: x / y == 2 or y / x == 2, two_divided_2)
    problem.addConstraint(lambda x, y, z: x + y + z == 10, ten_plus)

    sol = problem.getSolution()

    for i in range(0, n * n):
        if i % 4 == 3:
            print(sol[i])
            continue
        print(sol[i], end="\t")
