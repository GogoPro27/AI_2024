from constraint import *


def constraint_function(marija, simona, petar, meeting):
    marija_free_time = (14, 15, 18)
    simona_free_time = (13, 14, 16, 19)
    petar_free_time = (12, 13, 16, 17, 18, 19)

    if meeting not in simona_free_time or simona == 0:
        return False
    if meeting not in marija_free_time and marija == 1:
        return False
    if meeting not in petar_free_time and petar == 1:
        return False

    return petar + marija >= 1


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [12, 13, 14, 15, 16, 17, 18, 19])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(constraint_function,
                          ("Marija_prisustvo", "Simona_prisustvo", "Petar_prisustvo", "vreme_sostanok"))

    # ----------------------------------------------------

    # [print(solution) for solution in problem.getSolutions()]
    solutions = problem.getSolutions()

    for solution in solutions:
        reordered_solution = {'Simona_prisustvo': solution['Simona_prisustvo'],
                              'Marija_prisustvo': solution['Marija_prisustvo'],
                              'Petar_prisustvo': solution['Petar_prisustvo'],
                              'vreme_sostanok': solution['vreme_sostanok']}
        print(reordered_solution)