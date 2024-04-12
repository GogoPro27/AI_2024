from constraint import *


def sum_constraint(row):
    s = 0
    # print(row)
    for i in range(0, len(row)):
        if row[i] == '1':
            s += i + 1
    return s


def sum_cols_constraint(rows):
    sums = [0, 0, 0, 0]
    # print(rows)
    for i in range(0, 4):
        array = [rows[0][i], rows[1][i], rows[2][i], rows[3][i]]
        sums[i] = sum_constraint(array)
    return tuple(sums)


if __name__ == '__main__':
    n = 4
    variables = [i for i in range(1, n + 1)]
    variables = tuple(variables)
    # print(variables)
    domains = []
    for i in range(0, 2):
        for j in range(0, 2):
            for p in range(0, 2):
                for q in range(0, 2):
                    domains.append(str(i) + str(j) + str(p) + str(q))
    # print(domains)
    domains = tuple(domains)

    problem = Problem(BacktrackingSolver())
    problem.addVariables(variables, domains)

    sums_rows = (7, 7, 4, 5)
    sums_cols = (3, 4, 10, 3)

    for sum_row, row in zip(sums_rows, variables):
        # print(sum_row,row)
        problem.addConstraint(lambda r: sum_constraint(r) != sum_row, [row])

    problem.addConstraint(lambda *rows: sum_cols_constraint(rows) == sums_cols, variables)

    sol = problem.getSolutions()[1]
    for i in range(1, 5):
        s = sol[i]
        for letter in s:
            print(letter,end="\t")
        print()
