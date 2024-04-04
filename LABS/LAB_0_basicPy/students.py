import math
import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


def makeStudent(l1):
    return Student(l1[0], l1[1], l1[2])


def makeSubject(l1):
    return Subject(l1[0], int(l1[1]), int(l1[2]), int(l1[3]))


class Subject:
    def __init__(self, name, theory_points, practical_points, lab_points):
        self.name = name
        self.theory_points = theory_points
        self.practical_points = practical_points
        self.lab_points = lab_points

    def getGrade(self):
        grade = math.ceil((self.theory_points + self.practical_points + self.lab_points) / 10)
        if grade < 5:
            grade = 5
        return grade

    def __repr__(self):
        return f"----{self.name}: {self.getGrade()}"


class Student:
    def __init__(self, name='undefined', surname='undefined', index='undefined'):
        self.name = name
        self.surname = surname
        self.index = index
        self.subjects = []

    def addSubject(self, subject):
        self.subjects.append(subject)

    def __repr__(self):
        repr_string = f"Student: {self.name} {self.surname}\n"
        for subj in self.subjects:
            repr_string += str(subj) + "\n"
        return repr_string


if __name__ == "__main__":

    my_dic = {}

    while True:
        input_tmp = input()
        if input_tmp == "end":
            break
        input_list = input_tmp.split(",")
        idx = input_list[2]
        new_subj = makeSubject(input_list[3:])
        if idx not in my_dic.keys():
            new_student = makeStudent(input_list[:4])
            my_dic[idx] = new_student
        my_dic[idx].addSubject(new_subj)

    for key in my_dic:
        print(my_dic[key])
