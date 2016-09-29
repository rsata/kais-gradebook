import db
import os

def run(classes):
    os.system('clear')
    #KS set up the menu for Class Report using the string method .center
    title = ("Class Report")
    print(title.center(80, ' '))
    print()
    #KS set up values for menu to be able to format each string
    class_c = "Class"
    class_cn = "Class Name"
    class_ci = "Class Instructor"
    #KS use string method .ljust() to format each header 
    print(class_c.ljust(20) + class_cn.ljust(25) + class_ci.ljust(20))
    #KS Boolean to determine whether or not there are inputs in list classes
    found = False
    #KS for loop where report in classes is equal to each part of the sublist classes [0] - [2]
    #KS (0 being Class ID and 2 being Class Instructor)

    #get class lsit
    classes = db.db_get_classes()
    for class_info in classes:  
        # print (class_info[''])
        class_num = str(class_info['class_id'])
        class_name = class_info['class_name']
        class_teacher = class_info['class_instructor']        
        #KS prints each sublist under each header using string method .ljust()
        print(class_num.ljust(20) + class_name.ljust(25) + class_teacher.ljust(20))
        #KS make found = TRUE for Boolean
        found = True
    #KS if found remains False, print "No students found"
    if(not found):
        print("No classes found")
        
    print()        
    input("Press 'Enter' to Continue")
    print()
        



