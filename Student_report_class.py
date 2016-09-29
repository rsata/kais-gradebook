import os

def run(classes, students):
    os.system('clear')
    #KS set up the menu for Student Report by Class using the string method .center
    title = ("Student Report by Class")
    print(title.center(80, ' '))
    print()
    #KS set up values for menu to be able to format each string
    class_i = "Class ID"
    class_ci = "Class Instructor"
    student = "Student"
    grade = "Grade"
    #KS use string method .ljust() to format each header 
    print(class_i.ljust(20) + class_ci.ljust(26) + student.ljust(25) + grade.ljust(20))
    #KS Boolean to determine whether or not there are inputs in list classes and list students
    found = False
    #KS for loop where report_c in classes is equal to each part of sublist classes [0] and [2]
    #KS (0 being Class ID and 2 being Class Instructor)
    for report_c in classes:
        class_num = report_c[0]
        class_teacher = report_c[2]
        #KS for loop where report_c in classes is equal to each part of sublist classes [0], [2] - [4]
        #KS (0 being Class ID, 2 and 3 being Student First and Last Name and 4 being Grade)
        for report_s in students:
            #KS identify that Class ID from classes matches Class ID from students
            if class_num == report_s[0]:
                student = report_s[2] + " " + report_s[3]
                stu_grade = report_s[4]
                #KS prints each sublist under each header using string method .ljust()
                print(class_num.ljust(19), class_teacher.ljust(25), student.ljust(24), stu_grade.ljust(20))
                #KS make found = TRUE for Boolean
                found = True
    #KS if found remains False, print "No students found"
    if(not found):
        print ("No students matching classes found")

    print()
    input("Press 'Enter' to Continue")
    print()
        



