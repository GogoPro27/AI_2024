# Дадена ви е играта судоку. Во оваа игра во секој блок се ставаат бројки од 1 до 9
# така што во ниедна редица, колона и блок не смее да се повторува ниедна цифра.
# Почетно сите полиња се празни. Вашата задача е да најдете решение на овој проблем.
# Просторот ви е даден на сликата подолу.
#
# ![img.png](img.png)
#
# **Забелешка:** На влез добивате со каков `Solver` да работите.
# Испечатете го само првото решение. **Не е задолжително да ви поминуваат сите тест примери
# за задачата да биде точна. Зависи како сте ги поставиле условите.**
#
# Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи:
# AllDifferentConstraint, AllEqualConstraint, MaxSumConstraint, ExactSumConstraint,  MinSumConstraint,
# InSetConstraint, NotInSetConstraint, SomeInSetConstraint,  SomeNotInSetConstraint.

from constraint import *


def generate_block(num):
    l1 = []
    for i in range(0, 3):
        new_num = num + i
        for j in range(0, 3):
            l1.append(new_num + j * 9)
    return l1


if __name__ == '__main__':
    if __name__ == '__main__':
        type = input()
        problem = Problem(BacktrackingSolver())
        if type == "RecursiveBacktrackingSolver":
            problem = Problem(RecursiveBacktrackingSolver())
        if type == "MinConflictsSolver":
            problem = Problem(MinConflictsSolver())
        variables = tuple(range(81))
        domain = tuple(range(10))
        for variable in variables:
            problem.addVariable(variable, Domain(domain))

        # ---Tuka dodadete gi ogranichuvanjata----------------
        # 00 01 02 03 04 05 06 07 08
        # 09 10 11 12 13 14 15 16 17
        # 18 19 20 21 22 23 24 25 26
        # 27 28 29 30 31 32 33 34 35
        i = 0
        while i < 80:
            l1 = [a for a in range(i, i + 9)]
            problem.addConstraint(AllDifferentConstraint(), l1)
            # print(l1)
            i += 9
        i = 0
        while i < 9:
            l1 = []
            for j in range(0, 9):
                l1.append((j * 9) + i)
            # print(l1)
            problem.addConstraint(AllDifferentConstraint(), l1)
            i += 1
        l1 = []
        a = 3
        for i in range(0, 3):
            new_num = a * i
            for j in range(0, 3):
                l1.append(new_num + j * 27)
        # print(l1)
        for l in l1:
            whole_block = generate_block(l)
            problem.addConstraint(AllDifferentConstraint(), whole_block)
        # ----------------------------------------------------
        solution = problem.getSolution()
        for i in range(0,81):
            if i%9==8:
                print(solution[i],end="\n")
            else:
                print(solution[i],end="\t")
