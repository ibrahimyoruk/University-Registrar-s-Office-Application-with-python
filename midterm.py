def main():

    print("COURSE MANAGEMENT")
    print("--------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Available Courses")  # tamamlandı
    print("2 - Add Course")  # tamamlandı
    print("3 - Choosen Course")  # tamamlandı
    print("4 - Search Course With Number")  # tamamlandı
    print("5 - Search Course With Name")  # hata
    print("6 - Register to Course")
    print("7 - Liste Student Information")  # tamamlandı
    print("8 - Most Crowded courses")
    print("9 - Most Busy Students")

    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            viewCourses()
            break
        elif userChoice == '2':
            addCourse()
            break
        elif userChoice == '3':
            choosenCourse()
            break
        elif userChoice == '4':
            searchNum()
            break
        elif userChoice == '5':
            searchName()
            break
        elif userChoice == '6':
            registerCourse()
            break
        elif userChoice == '7':
            listStudentInf()
            break
        elif userChoice == '8':
            mostCrowdedCs()
            break
        elif userChoice == '9':
            mostBusyStd()


def viewCourses():
    print("VIEW COURSES")
    print("--------------")
    course = open("courses.txt", "r", encoding="utf-8")
    print(course.read())
    print()

    returnToMainMenu("MENU")

def addCourse():
    print("Add Course")
    print("-------------")
    courseId = input("write course code: ")
    courseName = input("write course name: ")
    courseIns = input("Write course instructor name: ")

    course_file = open("courses.txt", "a+", encoding="utf-8")
    with open("courses.txt", "a+", encoding="utf-8") as course_file:
        course_file.write(courseId + ";" + courseName + ";" + courseIns + ";" + "0" + ("\n"))

    course_file.close()
    returnToMainMenu("MENU")

def choosenCourse():
    print("Choosen Courses")
    print("----------------")
    print()
    course_file = open("courses.txt", "r", encoding="utf8")
    for i in course_file.readlines():
        a = i.split(";")
        if int(a[3]) == 0:
            continue
        else:
            print(a[0] + ";" + a[1] + ";" + a[2])
    returnToMainMenu("MENU")

def searchNum():
    print("Search with course id")
    print("----------------------")
    print()
    courseID = input("Enter course id: ")
    course_file = open("courses.txt", "r", encoding="utf8")
    codes = []
    for i in course_file.readlines():
        a = i.split(";")
        codes.append(a[0])
        if str(a[0]) == courseID:
            print(a[0] + ";" + a[1] + ";" + a[2] + ";" + a[3])
            break
        else:
            continue
    if courseID not in codes:
        print("The course cannot be found!!")

    returnToMainMenu("MENU")

def searchName():
    print("Seach with course name")
    print("-----------------------")
    print()
    course_name = input("Enter course name: ")
    course_file = open("courses.txt", "r", encoding="utf8")
    names = ""

    for i in course_file.readlines():
        a = i.split(";")
        names += str(a[1])
        if course_name in str(a[1]):
            print(a[0] + ";" + a[1] + ";" + a[2] + ";" + a[3])
        else:
            continue

    if course_name not in names:
        print("Course cannot be found!!")

    returnToMainMenu("MENU")

def registerCourse():
    print("REGISTER STUDENT TO COURSE")
    print("---------------------------")
    print()
    student_id = (input("Enter studen id: "))
    course_id = (input("Enter course id: "))
    student_file = open("students.txt", "r", encoding="utf8")
    lines = student_file.readline()
    empty_file = ""

    while (lines != ""):
        new_line = ""
        str = lines.split(";")
        if (str[0] == student_id):
            new_line = lines.rstrip() + ";" + course_id + "\n"
        else:
            new_Line = lines
        empty_file = empty_file + new_line
        lines = student_file.readline()

    write_file = open("students.txt", "w", encoding="utf8")
    write_file.close()
    student_file.close()

    returnToMainMenu("MENU")


def listStudentInf():
    print("WIEW STUDENTS INFORMATION")
    print("--------------------------")
    student = open("students.txt", "r", encoding="utf8")
    print(student.read())
    print()

    returnToMainMenu("MENU")


def mostCrowdedCs():
    print("Most Crowded 3 Course:")
    print("-----------------------")
    print()
    courses = []
    studentsCount = []

    with open("courses.txt", "r", encoding="utf-8") as file:
        for line in file:
            piece = line.split(";")
            courses.append(piece[1])
            studentsCount.append(int(piece[3]))
        top3 = []
        for i in range(3):
            value = max(studentsCount)
            index_value = studentsCount.index(value)
            top3.append(courses[index_value])
            studentsCount[index_value] = 0
    a = 1
    print()
    for i in top3:
        print(a, "----", i)
        a += 1
    returnToMainMenu("MENU")


def mostBusyStd():
    print("Most Crowded 3 Student:")
    print("-----------------------")
    print()

    with open("students.txt", "r", encoding="utf-8") as file:
        students = []
        courseCount = []
        for lines in file:
            category = lines.split(";")
            lessons = category[2].split(",")
            students.append(category[1])
            courseCount.append(len(lessons))

        top3 = []

        for i in range(3):
            value = max(courseCount)
            index_value = courseCount.index(value)
            top3.append(students[index_value])
            courseCount[index_value] = 0
    a = 1
    for i in top3:
        print(a, "----", i)
        a += 1
    returnToMainMenu("MENU")


def returnToMainMenu(message):
    while True:
        print()
        back = input(f"{message}. Press (M) To Return To Main Menu: ").lower() if message != None else input(
            "Press (M) To Return To Main Menu: ").lower()
        if back == 'm':
            main()
            break


main()
