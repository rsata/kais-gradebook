import db
import os

def run(students):
    os.system ('clear')
    #KS set up the menu for Student Record using the string method .center
    title = ("Add a Student Record")
    print(title.center(80, ' '))
    print()
    #KS run input_students
    input_student(students)
    print("Student successfully added!")
    print()
    #KS create an infinite loop where user has to pick "Yes" or "No" to exit the loop
    while (True):
        again = str(input("Add another student record? (Yes or No): "))
        while again != "Yes" and again != "No":
            print("Invalid Input")
            again = str(input("Add another student record? (Yes or No): "))
            #KS if "Yes" re-run input_students
        if again == "Yes":
            classes = input_student(students)
            print("Student successfully added!")
            print()
            #KS if "No" return to the home menu and return students
        if again == "No":
            print()
            return students

#KS define input_students
def input_student(students):
    #KS prepare the list students to be appended
    students.append([])
    #KS prompt the user to input information
    student_class_id = int(input("Class ID:                "))
    student_id = int(input("Student ID:              "))
    student_first_name = str(input("Student First Name:      "))
    student_last_name = str(input("Student Last Name:       "))
    student_grade = int(input("Student Grade:           "))

    #save to db
    db.db_save_student(student_class_id, student_id, student_first_name, student_last_name, student_grade)

    #KS take length of list students and subtract one to get the last item in the list
    #KS then add the inputs from before to a sublist of students
    #KS each entry is adding onto this sublist from the inputs above
    students[len(students)-1].append(student_class_id)
    students[len(students)-1].append(student_id)
    students[len(students)-1].append(student_first_name)
    students[len(students)-1].append(student_last_name)
    students[len(students)-1].append(student_grade)
    return students
