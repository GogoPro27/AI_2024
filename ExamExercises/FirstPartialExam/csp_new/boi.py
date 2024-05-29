from constraint import *

if __name__ == '__main__':
    variables = ["A", "B", "C", "D", "E", "F"]
    domains = ["red", "green", "blue"]

    problem = Problem(BacktrackingSolver())
    problem.addVariables(variables, domains)

    problem.addConstraint(lambda x: x == "blue", "A")
    problem.addConstraint(lambda x: x == "green", "B")
    problem.addConstraint(lambda x: x == "red", "F")

    group1 = ["A","B","C"]
    group2 = ["B","C","D"]
    group3 = ["C","D","E"]
    group4 = ["F","D","E"]

    for group in group1,group2,group3,group4:
        problem.addConstraint(AllDifferentConstraint(),group)

    print(problem.getSolution())
