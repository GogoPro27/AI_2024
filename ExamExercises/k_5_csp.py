from constraint import *


def ml_constraint(*ML_domains):
    hours = []

    for d in ML_domains:
        hours.append(d.split("_")[1])

    return len(hours) == len(set(hours))


def different_time_constraint(a, b):
    d1, t1 = a.split("_")
    d2, t2 = b.split("_")
    if d1 == d2 and abs(int(t1) - int(t2)) <= 1:
        return False
    return True


# dokolku trebashe da bidat eden do drug
# def sequential_constraint(*subject_domains):
#     if len(subject_domains) == 1:
#         return True
#     hours = []
#     days = []
#     print(subject_domains)
#     for d in subject_domains:
#         hours.append(int(d.split("_")[1]))
#         days.append(d.split("_")[0])
#
#     if len(set(days)) != 1:
#         return False
#     hours.sort()
#     print(hours)
#     return hours[-1] - hours[0] == len(hours) - 1


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    vars_AI = []
    for i in range(1, casovi_AI + 1):
        vars_AI.append(f"AI_cas_{i}")

    vars_ML = []
    for i in range(1, casovi_ML + 1):
        vars_ML.append(f"ML_cas_{i}")

    vars_R = []
    for i in range(1, casovi_R + 1):
        vars_R.append(f"R_cas_{i}")

    vars_BI = []
    for i in range(1, casovi_BI + 1):
        vars_BI.append(f"BI_cas_{i}")

    # print(vars_AI, vars_BI, vars_R, vars_ML)

    problem.addVariables(vars_AI, AI_predavanja_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)

    problem.addVariables(vars_ML, ML_predavanja_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)

    problem.addVariables(vars_R, R_predavanja_domain)

    problem.addVariables(vars_BI, BI_predavanja_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    all_vars = vars_AI + vars_ML + vars_R + vars_BI + ["ML_vezbi", "BI_vezbi", "AI_vezbi"];

    for var1 in all_vars:
        for var2 in all_vars:
            if var1 == var2:
                continue
            problem.addConstraint(different_time_constraint, (var1, var2))

    problem.addConstraint(ml_constraint, vars_ML + ["ML_vezbi"])

    # dolkolku trebashe da bidat eden do drug:
    # problem.addConstraint(sequential_constraint, vars_AI)
    # problem.addConstraint(sequential_constraint, vars_BI)
    # problem.addConstraint(sequential_constraint, vars_R)
    # problem.addConstraint(sequential_constraint, vars_ML)

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
