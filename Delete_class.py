import db
import os

def run(classes):
    os.system('clear')
    #KS set up the menu for Delete a Class Record using the string method .center
    title = ("Delete a Class Record")
    print(title.center(80, ' '))
    print()

    delete(classes)   
    print()
    #KS create an infinite loop where user has to pick "Yes" or "No" to exit the loop
    while(True):
        again = str(input("Delete another class record? (Yes or No): "))
        while again != "Yes" and again != "No":
            print("Invalid Input")
            again = str(input("Delete another class record? (Yes or No): "))
            #KS if "Yes" re-run delete(classes)
        if again == "Yes":
            classes = delete(classes)
            print()
            #KS if "No" return to the home menu and return classes
        if again == "No":
            print()
            return classes
    
#KS define delete
def delete(classes):
    #KS prompt user for the Class ID of desired to be deleted
    removal_id = str(input("Class ID:      "))
    
    db.db_delete_class(removal_id)

    #KS if found remains False, print "Class does not exist"
    # if(not found):
    #     print("Class does not exist")

    return classes
    
    
    
