from constraint import *


# var    #domain     #dic
def max_4_constraint(*paperIDs_domains):
    check_my_dic = {}
    # print(paperIDs_domains)

    # only 4 in one termin
    for termin in paperIDs_domains:
        if termin not in check_my_dic.keys():
            check_my_dic[termin] = 1
        else:
            check_my_dic[termin] = check_my_dic.get(termin) + 1
    for value in check_my_dic.values():
        if value > 4:
            return False

    return True


def must_be_in_same_termin(*paperIds_domains):
    return len(set(paperIds_domains)) == 1


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = [var + f" ({papers[var]})" for var in papers.keys()]
    # print(variables)

    domain = [f'T{i + 1}' for i in range(num)]
    # print(domain)

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(max_4_constraint, tuple(variables))
    oblasti = tuple(set(papers.values()))
    # print(oblasti)
    for oblast in oblasti:
        l1 = []
        for var in variables:
            if oblast in var:
                l1.append(var)
        # print(l1)
        if len(l1) <= 4:
            problem.addConstraint(must_be_in_same_termin, l1)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    for v in variables:
        print(v + ": " + result[v])
