from constraint import *

if __name__ == '__main__':
    problem = Problem()
    variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
    domains = ["red", "green", "blue"]
    problem.addVariables(variables, domains)
    forbidden_pairs = [("WA", "NT"), ("WA", "SA"), ("SA", "NT"), ("SA", "NSW"), ("SA", "Q"), ("SA", "V"), ("NT", "Q"),
                       ("Q", "NSW"), ("NSW", "V")]
    for pair in forbidden_pairs:
        problem.addConstraint(lambda a, b: a != b, pair)  # ustvari domenite da ne im se isti
    print(problem.getSolution())
    print(problem.getSolutions())
    print()
    res_iter = problem.getSolutionIter()
    for i in range(5):
        print(next(res_iter))
