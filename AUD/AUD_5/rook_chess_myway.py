from constraint import *

problem = Problem()

variables = []
for i in range(8):
    for j in range(8):
        variables.append((i, j))
domains = [0, 1]
problem.addVariables(variables, domains)

for row in range(0, 8):
    coord_row = [(row, col) for col in range(8)]
    problem.addConstraint(ExactSumConstraint(1), coord_row)

for col in range(0, 8):
    coord_col = [(row, col) for row in range(8)]
    problem.addConstraint(ExactSumConstraint(1), coord_col)

# print(problem.getSolution())
# sol = problem.getSolution()
sols = problem.getSolutions()
for sol in sols:
    for i in range(8):
        for j in range(8):
            print(sol[(i, j)], end=' ')
        print()
    print()
    print()
    print()
