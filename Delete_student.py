import db
import os

def run(students):
    os.system('clear')
    #KS set up the menu for Delete a Student Record using the string method .center
    title = ("Delete a Student Record")
    print(title.center(80, ' '))
    print()
    
    delete(students)
    print()
    while(True):
        #KS create an infinite loop where user has to pick "Yes" or "No" to exit the loop
        again = str(input("Delete another student record? (Yes or No): "))
        while again != "Yes" and again != "No":
            print("Invalid Input")
            again = str(input("Delete another student record? (Yes or No): "))
        if again == "Yes":
            #KS if "Yes" re-run delete(students)
            students = delete(students)
            print()
            #KS if "No" return to the home menu and return students
        if again == "No":
            print()
            return students

#KS define delete
def delete(students):
    #KS prompt user for the Class ID and Student ID of desired to be deleted
    removal_cl_id = str(input("Class ID:        "))
    removal_st_id = str(input("Student ID:      "))

    db.db_delete_student(removal_st_id, removal_cl_id)
    
    # #KS if found remains False, print "Student does not exist"        
    # if(not found):
    #     print("Student does not exist")
        
    return students
