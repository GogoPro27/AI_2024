from constraint import *

if __name__ == '__main__':
    problem = Problem(RecursiveBacktrackingSolver())

    words = ["set", "cyber", "pod", "myman", "faked", "cross", "elite", "ebike", "met", "rod", "naked", "new", "amino",
             "net", "pakman", "sudoku"]
    problem.addVariables((5, 8), tuple([word for word in words if len(word) == 3]))
    problem.addVariables((1, 2, 3, 4, 6, 7), tuple([word for word in words if len(word) == 5]))

    problem.addConstraint(lambda x, y: x[1] == y[1], (4, 1))
    problem.addConstraint(lambda x, y: x[2] == y[1], (4, 2))
    problem.addConstraint(lambda x, y: x[3] == y[1], (4, 3))
    problem.addConstraint(lambda x, y: x[-1] == y[0], (4, 5))

    problem.addConstraint(lambda x, y: x[1] == y[2], (6, 1))
    problem.addConstraint(lambda x, y: x[2] == y[2], (6, 2))
    problem.addConstraint(lambda x, y: x[3] == y[2], (6, 3))
    problem.addConstraint(lambda x, y: x[-1] == y[1], (6, 5))

    problem.addConstraint(lambda x, y: x[1] == y[3], (7, 1))
    problem.addConstraint(lambda x, y: x[2] == y[3], (7, 2))
    problem.addConstraint(lambda x, y: x[3] == y[3], (7, 3))
    problem.addConstraint(lambda x, y: x[-1] == y[2], (7, 5))

    problem.addConstraint(lambda x, y: x[-1] == y[0], (4, 5))
    problem.addConstraint(lambda x, y: x[-1] == y[1], (6, 5))
    problem.addConstraint(lambda x, y: x[-1] == y[2], (7, 5))

    sol = problem.getSolution()

    print(sol)
