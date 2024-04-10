from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(lambda a, b, c: a + b == c, ("D", "E", "Y"))
    problem.addConstraint(lambda a, b, c: a + b == c, ("N", "R", "Y"))
    # ----------------------------------------------------

    # print(problem.getSolution())
