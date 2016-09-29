import db
import os

def run(students):
    os.system('clear')
    #KS set up the menu for Student Report using the string method .center
    title = ("Student Report")
    print(title.center(80, ' '))
    print()
    #KS set up values for menu to be able to format each string
    class_i = "Class ID"
    student_i = "Student ID"
    student = "Student"
    grade = "Grade"
    #KS use string method .ljust() to format each header 
    print(class_i.ljust(20) + student_i.ljust(20) + student.ljust(20) + grade.ljust(20))
    #KS Boolean to determine whether or not there are inputs in list students
    found = False
    #KS for loop where report in students is equal to each part of the sublist students [0]-[4]
    #KS (0 being Class ID and 4 being Grade)

    students = db.db_get_students()
    for student in students:
        class_num = str(student['class_id'])
        student_num = str(student['student_id'])
        student_name = student['student_first_name'] + " " + student['student_last_name']
        stu_grade = str(student['student_grade'])
        #KS prints each sublist under each header using string method .ljust()
        print(class_num.ljust(20) + student_num.ljust(20) + student_name.ljust(20) + stu_grade.ljust(20))
        #KS make found = TRUE for Boolean
        found = True
    #KS if found remains False, print "No students found"
    if(not found):
        print("No students found")
        
    print()
    input("Press 'Enter' to Continue")
    print()

    
