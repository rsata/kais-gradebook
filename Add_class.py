#KS add_class program
import db
import os

#KS define run
def run(classes):
    os.system ('clear')
    #KS set up the menu for Class Record using the string method .center
    title = ("Add a Class Record")
    print(title.center(80, ' '))
    print()
    #KS run input_classes
    input_class(classes)
    print("Class successfully added!")
    print()
    #KS create an infinite loop where user has to pick "Yes" or "No" to exit the loop
    while (True):
        again = str(input("Add another class record? (Yes or No): "))
        while again != "Yes" and again != "No":
            print("Invalid Input")
            again = str(input("Add another class record? (Yes or No): "))
            #KS if "Yes" re-run input_class
        if again == "Yes":
            classes = input_class(classes)
            print("Class successfully added!")
            print()
            #KS if "No" return to the home menu and return classes
        if again == "No":
            print()
            return classes 
  
#KS define input_class        
def input_class(classes):
        #KS prepare the list classes to be appended
        classes.append([])
        #KS prompt the user to input information
        class_id = str(input("Class ID:              ")) 
        class_name = str(input("Class name:            "))
        class_instructor = str(input("Class Instructor:      "))

        db.db_save_class(class_id, class_name, class_instructor)

        #KS take length of list classes and subtract one to get the last item in the list
        #KS then add the inputs from before to a sublist of classes
        #KS each entry is adding onto this sublist from the inputs above
        classes[len(classes)-1].append(class_id)
        classes[len(classes)-1].append(class_name)
        classes[len(classes)-1].append(class_instructor)
        return classes
        
    

    
