#--------------------To-Do List program----------------------------

#--->Function for displaying all task in To-Do list
def showList(todo):
    if len(todo)==0:
        print("Your To-Do List is Empty.\nTry adding a new task.")
    else:
        for i in range(len(todo)):
            print(f"{i+1}) {todo[i]}") #test this

#--->Function for adding a new task in the To-Do list
def addTask(todo):
    task=input("\nEnter the task to add in To-Do list: ")
    todo.append(task)
    print("Task added in the To-Do list successfully!")
    option=input("Do you wish to add another task (Y or N): ")
    opt=option.capitalize()
    if opt=='Y':
        addTask(todo)
    elif opt=='N':
        return
    else:
        print("Invalid input!")
        return

#--->Function for Updating any task in the To-Do list
def updateTask(todo):
    if len(todo)==0:
        print("Your To-Do List is Empty.\nTry adding a new task.")
    else:
        showList(todo)
        task_no=int(input("\nEnter the task number you wish to update: "))
        if task_no>=1 and task_no<=len(todo):
            updated_task=input("Enter the task to update: ")
            todo[task_no-1]=updated_task
            print("Task updated successfully!")
        else:
            print("Invalid input. Try Again with correct number!")

#--->Function for deleting any task from the To-Do list
def deleteTask(todo):
    if len(todo)==0:
        print("Your To-Do List is Empty.\nTry adding a new task.")
    else:
        showList(todo)
        del_no=int(input("\nEnter the task number you wish to delete: "))
        if del_no>=1 and del_no<=len(todo):
            del todo[del_no-1]
        else:
            print("Invalid input. Try Again with correct number!")

#--->Function for showing the menu with options of To-Do list to the user
def menu():
    print("\nTo-Do List: \n")
    print("1. Show Task List")
    print("2. Add New Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. EXIT")
    c = input("\nEnter your choice (1-5): ")
    return c

#--->Program execution start from here
todo=[]
while True:
    choice = menu() 
    if choice=="1":
        showList(todo)
    elif choice=="2":
        addTask(todo)
    elif choice=="3":
        updateTask(todo)
    elif choice=="4":
        deleteTask(todo)
    elif choice=="5":
        print("Exiting from To-Do List...")
        break
    else:
        print("Invalid input. Try Again with correct number!")
