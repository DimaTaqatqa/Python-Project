from Admin import *
from Student import *
import os
import matplotlib.pyplot as plt


cour = []
file_data = {}
courses_list = []

# function to read the computer_engineering file which contains all ENCS & ENEE courses and make a list of objects from course class
def read_course():
    file_c = open("computer_engineering.txt", "r")
    info = file_c.readlines()
    for line in info:#splitting and making and append the course object to the list
        li = line.split(";")
        n = str(li[0])
        p = n.split(":")
        name = p[0]
        hours = int(li[1])
        semesters = li[2]
        years = int(li[3])
        grade = li[len(li) - 1]
        file_data[name] = hours
        c = Course(name, hours, semesters, years, grade)
        courses_list.append(c)


read_course()

# function to check if id number is valid or not
def is_id(ss):
    # id is valid when it contains 7 digits and all of them are numbers
    if ss.isdigit():
        n = int(ss)
        c = 0
        while n > 0:
            c = c + 1
            n = n // 10
        if c != 7:
            return False
        else:
            return True
    else:
        return False

# function to read every student file and make a student object with add the taken courses with their hours
def read_student(stud_id):
    c0 = [Course("", 0, 0, 0, 0)]
    name = ""
    hour = ""
    semester_s = ""
    years = ""
    grade = ""
    std_file = open(stud_id + ".txt", "r")
    next(std_file)
    for line in std_file:
        slash = line.split("/")
        years = slash[0]
        semi = slash[1].split(";")
        semester_s = semi[0]
        com = semi[1].split(",")
        for i in range(len(com)):
            sp = com[i].split(" ")
            name = sp[1]
            grade = sp[2]
            hour = file_data.get(name)
            c0.append(Course(name, hour, semester_s, years, grade))
    student = Student("student", stud_id, stud_id, c0)
    student.add_course(name, hour, semester_s, years, grade)
    return c0

# function to edit the grade of a specific course
def edit(id, nn, ng):
    c = read_student(id) # to read the student file and return a list of taken courses with their names, grades, and hours
    y = ""
    s = ""
    nfc = ""
    l = []
    with open(id + '.txt', 'r+') as myfile:
        lines = myfile.readlines()
        myfile.seek(0)
        myfile.truncate()
        myfile.write("Year/Semester ; Courses with grades\n")
        lookup = ", "
        n = 0
        for i in range(1, len(lines)):
            slash = lines[i].split("/")
            years = slash[0]
            semi = slash[1].split(";")
            semester_s = semi[0]
            com = semi[1].split(",")
            myfile.write(years + "/" + semester_s + "; ")
            for j in range(len(com)):
                sp = com[j].split(" ")
                c[j].name = sp[1]
                if c[j].name == nn:
                    c[j].grades = ng
                else:
                    c[j].grades = sp[2]
                myfile.write(c[j].name + " " + c[j].grades + ", ")
            myfile.write("\n")
    myfile.close()
    f = open(id + ".txt", "r+")
    liness = f.readlines()
    f.seek(0)
    f.truncate()
    for line in liness:
        if len(line.strip()) >= 2:
            f.write(line)
    with open(id + ".txt", "rb+") as f:
        f.seek(f.tell() - 4, 2)
        f.truncate()
        print(f.read())

# function to get the number od taken hours
def get_hours(id):
    c = read_student(id) # to read the student file and return a list of taken courses with their names, grades, and hours
    k = []
    for i in range(1, len(c) - 1):
        v = c[i].name
        s = file_data.get(v)
        k.append(s)
    sm = sum(k)
    return sm

# function to get the average number of hours per semester
def h_per_s(id):
    c = read_student(id)# to read the student file and return a list of taken courses with their names, grades, and hours
    h = get_hours(id)
    k = []
    y = []
    s = []
    n_s = 0
    fle = open(id + ".txt", "r+")
    content = fle.read()
    lines = content.split("\n")
    fle.close()
    n_s = len(lines) - 1
    ans = h / n_s
    return ans

# function that print a list of the remaining courses
def r_c(id):
    c = read_student(id) # to read the student file and return a list of taken courses with their names, grades, and hours
    key_list = list(file_data.keys())
    for i in range(1, len(c)):
        for j in range(len(key_list) - 1):
            if key_list[j] == c[i].name:
                key_list.remove(c[i].name)
    print(key_list)

# function to plot the grade distribution for a specific student
def plot_g_d(id):
    c = read_student(id) # to read the student file and return a list of taken courses with their names, grades, and hours
    names = []
    grades = []

    for i in range(1, len(c) - 1):
        names.append(c[i].name)
        grades.append(int(c[i].grades))

    plt.figure(figsize=(10, 10))
    plt.bar(names, grades, align='center',  width=0.5)
    plt.title('grades distribution for '+ id)
    plt.xlabel('Courses')
    plt.ylabel('Grades')
    plt.show()

# function to return the average per semester
def get_avg(id, yr, sem):
    c = read_student(id) # to read the student file and return a list of taken courses with their names, grades, and hours
    key_list = list(file_data.keys())
    val_list = list(file_data.values())
    s1 = []
    ho = []
    y = []
    s = []
    n = []
    g = []
    g1 = []
    hour = []
    grade = []
    year_ = []
    names = []
    check_y = 0
    check_s = 0
    for i in range(1, len(c) - 1):
        y.append(c[i].year)
        s.append(c[i].semester)
        n.append(c[i].name)
        g.append(c[i].grades)

    for k in range(len(n)):
        for m in range(len(key_list)):
            if n[k] == key_list[m]:
                ho.append(val_list[m])

    for element in s:
        s1.append(element.strip())

    for element in g:
        g1.append(element.strip())

    for j in range(len(n)):
        if y[j] == str(yr) and int(s1[j]) == int(sem):
            hour.append(ho[j])
            grade.append(g1[j])
            names.append(n[j])

    for k in range(len(hour)):
        ps = float(float(hour[k]) * float(grade[k]))
        year_.append(float(ps))

    h = sum(hour)
    l = sum(year_)
    avg = float(l / h)
    return avg

# function to return the overall average
def avg_sem(id):
    c = read_student(id)
    l = []
    l1 = []

    for j in range(1, len(c)-1):
        y1 = c[j].year
        s1 = c[j].semester
        a1 = get_avg(id, y1, s1)
        l.append(a1)

    for j in l:
        if j not in l1:
            l1.append(j)
    sm = sum(l1)
    ans = sm / len(l1)
    return ans

# to login as admin or student
login = input("please choose a user  admin or student (1 for admin 2 for student):\n")
if login == '1':
    id = input("please enter your id\n")
    if is_id(id):
        password = input("please enter the password\n")
        admin1 = Admin("admin", id, password)
        while True:
            ans1 = 0
            Admin.display_menu_admin(admin1)
            select = input("please enter your selection:\n")
            if select == '1':
                student_id = input("please enter the student id\n")
                if is_id(student_id):
                    file = open(student_id + ".txt", "a")
                    file.write("Year/Semester ; Courses with grades\n")
                    year = input("write the years(year-year):\n")
                    semester = input("write the semester:\n")
                    courses = input("write the name of the courses:\n")
                    grades = input("write the grade for the previous course:\n")
                    file.write(year + "/" + semester + " ; " + courses + " " + grades)
                    ans0 = input("do you want to add more courses?\n")
                    if ans0 == "yes":
                        ans1 = input("write the number of courses you want to add:\n")
                    for i in range(int(ans1)):
                        courses1 = input("write the name of the course:\n")
                        grades1 = input("write the grade for the previous course:\n")
                        file.write(", " + courses1 + " " + grades1)

                    file.close()

            elif select == "2":
                student_id = input("write the student id that you want to add a semester to:\n")
                file_exists = os.path.exists(student_id + ".txt")
                if file_exists:
                    file = open(student_id + ".txt", "a")
                    year = input("write the years(year-year):\n")
                    semester = input("write which semester:\n")
                    courses = input("write the name of the course:\n")
                    grades = input("write the grade for the previous course:\n")
                    file.write("\n" + year + "/" + semester + " ; " + courses + " " + grades)
                    ans0 = input("do you want to add more courses?\n")
                    if ans0 == "yes":
                        ans1 = input("write the number of courses you want to add:\n")
                    for i in range(int(ans1)):
                        courses1 = input("write the name of the course:\n")
                        grades1 = input("write the grade for the previous course:\n")
                        file.write(", " + courses1 + " " + grades1)

                    else:
                        file.close()
                else:
                    print("you need to add a new record first.\n")

            elif select == "3":
                student_id = input("write the student id that you want to update the grade for:\n")
                course = input("write the name of the course that you want to update the grade for:\n ")
                new = input("write the new grade:\n")
                edit(student_id, course, new)
            elif select == "4":
                id_s = input("Enter the id for the student you want to see statics for:\n")
                yr = input("whats the year of the semester you want to get the average for(year-year):\n")
                sem = input("which semester of this year you want:\n")
                get_hours(id_s)
                print("taken hours :" + str(get_hours(id_s)))
                print("remaining courses :")
                r_c(id_s)
                print("average :" + str(get_avg(id_s, yr, sem)))
                print("overall average: " + str(avg_sem(id_s)))

            elif select == "5":

                all=input("enter the id number of the students you want to get statistics for them respectively (add space between id numbers)\n")
                all_id=all.split(" ")
                for i in range(len(all_id)):
                    a1 = avg_sem(str(all_id[i]))
                    h1 = h_per_s(str(all_id[i]))
                    print("the overall average for the student " + all_id[i] + " is: " + str(a1) + " and the average hours per semester is: " + str(h1))
                    plot_g_d(str(all_id[i]))

            elif select == "6":
                all = input("enter the id number of the students you want to get statistics for them respectively add space between id numbers\n")
                all_id = all.split(" ")
                print("retrieve id:\n1) based on average.\n2) based on taken hours.\n")
                selection = input("choose what you want:\n")
                if selection == "1":
                    avg = input("please enter what average you want:\n")

                    for i in range(len(all_id)):
                        a1 = avg_sem(str(all_id[i]))
                        if a1 > float(avg):
                            print("the student that has the id " + all_id[i] + " has an average greater than " + avg)
                        elif a1 == float(avg):
                            print("the student that has the id " + all_id[i] + " has an average equal to " + avg)
                        else:
                            print("the student that has the id " + all_id[i] + " has an average less than " + avg)


                if selection == "2":
                    hour = input("please enter the number of hours you want:\n")

                    for i in range(len(all_id)):
                        h1 = get_hours(str(all_id[i]))

                        if h1 > int(hour):
                            print("the student that has the id " + all_id[i] + " has finished hours greater than " + hour +" hours")
                        elif h1 == int(hour):
                            print("the student that has the id " + all_id[i] + " has finished " + hour + " hours")
                        else:
                            print("the student that has the id " + all_id[i] + " has finished hours less than " + hour + " hours")


            elif select == "7":
                exit(0)
            else:
                print("error, invalid selection input")

elif login == '2':
    id = input("please enter your id\n")
    if is_id(id):
        password = input("please enter the password\n")
        student1 = Student("student", id, password, cour)
        while True:
            Student.display_menu_student(student1)
            select = input("please enter your selection:\n")
            if select == '1':
                yr = input("whats the year of the semester you want to get the average for(year-year):\n")
                sem = input("which semester of this year you want:\n")
                get_hours(id)
                print("taken hours :" + str(get_hours(id)))
                print("remaining courses :")
                r_c(id)
                print("average :" + str(get_avg(id, yr, sem)))
                print("overall average: " + str(avg_sem(id)))

            elif select=='2':

                a1 = avg_sem(id)
                h1 = h_per_s(id)
                print("the overall average for the student " + id + " is: " + str(
                        a1) + " and the average hours per semester is: " + str(h1))
                plot_g_d(id)
            elif select=='3':
                exit(0)
            else:
                print("error, invalid selection input")

else:
    print("error, id number is invalid")