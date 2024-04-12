from constraint import *


def max4(*termins):
    dic = dict()
    for t in termins:
        if dic.__contains__(t):
            dic[t] = dic[t] + 1
        else:
            dic[t] = 1
    if len([val for val in dic.values() if val > 4]) >= 1:
        return False
    return True


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite

    # print(papers)
    variables = [f"{key} ({val})" for key, val in papers.items()]
    domain = [f'T{i + 1}' for i in range(num)]

    # print(variables)
    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    dic_by_oblast = {}
    for var in variables:
        oblast = var[-4:-2]
        if dic_by_oblast.__contains__(oblast):
            dic_by_oblast[oblast].append(var)
        else:
            dic_by_oblast[oblast] = []
            dic_by_oblast[oblast].append(var)
    # print(dic_by_oblast)

    for value in dic_by_oblast.values():
        # print(value)
        if len(value) <= 4:
            problem.addConstraint(AllEqualConstraint(), value)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(max4, variables)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    for var in variables:
        print(f"{var}: {result[var]}")
