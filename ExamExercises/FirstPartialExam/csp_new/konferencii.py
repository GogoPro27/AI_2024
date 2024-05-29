from constraint import *


def consecutive_conf_constraint(*days):
    a = days[0]
    b = days[1]
    c = days[2]
    d = days[3]
    # print(a,b,c,d)
    if a[-1] >= b[-1] or a[-1] >= c[-1]:
        return False
    if b[-1] >= d[-1]:
        return False
    if c[-1] >= d[-1]:
        return False
    return True

if __name__ == '__main__':

    variables = ["A", "B", "C", "D"]
    domains = []
    days = [1,2,3,4,5,6,7,8,9,10]
    days_triples = []
    for i in range(len(days)-3):
        days_triples.append(days[i:i+4])
    days_quarts = []
    for i in range(len(days) - 2):
        days_quarts.append(days[i:i + 3])

    # print(days_quarts)
    # print(days_triples)

    problem = Problem(BacktrackingSolver())
    problem.addVariables(["B","C"], days_quarts)
    problem.addVariables(["A","D"], days_triples)

    problem.addConstraint(consecutive_conf_constraint, variables)
    print(problem.getSolution())