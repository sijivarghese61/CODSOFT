#---------------------------------SIMPLE CALCULATOR PROGRAM----------------------------------

#--->Function for ADDITION of two numbers
def addition():
    return num1+num2

#--->Function for SUBTRACTION of two numbers
def subtraction():
    return num1-num2

#--->Function for MULTIPLICATION of two numbers
def multiplication():
    return num1*num2

#--->Function for DIVISION of two numbers
def division():
    if num2==0:
        return "Any number divided by Zero is undefined!"
    return num1/num2

#--->Function for showing the OPERATIONS of calculator to the user
def menu():
    print("\nCALCULATOR\n")
    print("Operations:-")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. EXIT")
    c=input("Enter the operation number you want to perform (1-5): ")
    return c
#--->Program execution start from here
while True:
    operations=['Addition','Subtraction','Multiplication','Division']
    list_opt=['1','2','3','4']
    choice=menu()
    if choice=="5":
        print("EXITING from Calculator...")
        break
    elif choice not in list_opt:
        print("Invalid input. Try Again with correct number!")
    else:
        operation=operations[int(choice)-1]
        num1=float(input(f"Enter First Number to perform the {operation}: "))
        num2=float(input(f"Enter Second Number to perform the {operation}: "))
        if choice=="1":
            result=addition()
        elif choice=="2":
            result=subtraction()
        elif choice=="3":
            result=multiplication()
        elif choice=="4":
            result=division()
        print(f"The Result of {operation} of {num1} and {num2} is: {result}")
