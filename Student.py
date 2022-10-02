from Course import *
from User import *


class Student(User):
    cour = [Course("", 0, 0, 0, 0)]

    def __init__(self, username, id, password, cour):
        super().__init__(username, id, password)
        self.cour = cour

    def add_course(self, name, hours, semester, year, grades):
        self.cour.append(Course(name, hours, semester, year, grades))

    def set_course(self, name, hours, semester, year, grades):
        self.cour = []
        self.cour.append(Course(name, hours, semester, year, grades))

    def get_course(self, i):
        return self.cour[i]

    def get_c(self):
        return self.cour

    def display_menu_student(self):
        print("********MAIN MENU*********\n1)Student statistics\n2)Global statistics\n3)Exit")
