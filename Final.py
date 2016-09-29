#Reginal Database Management System
#6/1/2016
#Kai Sata
#Program that takes data and can edit it then report it each time it is called

#KS import all external programs that will be called later on in the user choice
import Add_class
import Class_report
import Delete_class
import Add_student
import Delete_student
import Student_report
import Student_report_class
import os

#KS define user choice
def user_choice():
    os.system('clear')
    #KS set classes and students to empty lists to be appended later on
    classes = []
    students = []
    #KS create spacing for title screen using title.center to center it
    title = "Class Roster Database"
    print(title.center(80, ' '))
    print()
    #KS print all options available for user choice
    print("1. Add a Class")
    print("2. Add a Student")
    print("3. Delete a Class Record")
    print("4. Delete a Student Record")
    print("5. Class Report")
    print("6. Student Report")
    print("7. Student Report by Class")
    print("8. Exit")
    print()
    #KS user can input their choice
    choice = str(input("Please choose: "))
    print()
    #KS if the user inputs any choice that is not 8 the program will run one of the options
    while choice != 8:
        if choice == "1":
            classes = Add_class.run(classes)
        if choice == "2":
            students = Add_student.run(students)
        if choice == "3":
            classes = Delete_class.run(classes)
        if choice == "4":
            students = Delete_student.run(students)
        if choice == "5":
            Class_report.run(classes)
        if choice == "6":
            Student_report.run(students)
        if choice == "7":
            Student_report_class.run(classes, students)
        if choice == "8":
            break
        #KS if no number between 1 and 7 (8 will exit the program) re-print the title screen
        title = "Class Roster Database"
        print(title.center(80, ' '))
        print()
        print("1. Add a Class")
        print("2. Add a Student")
        print("3. Delete a Class Record")
        print("4. Delete a Student Record")
        print("5. Class Report")
        print("6. Student Report")
        print("7. Student Report by Class")
        print("8. Exit")
        print()
        choice = str(input("Please choose: "))
        print()
        
        
#KS cs call to user_choice
user_choice()

