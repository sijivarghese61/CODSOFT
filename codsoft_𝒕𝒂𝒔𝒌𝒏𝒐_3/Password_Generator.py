#--------------------------------PASSWORD GENERATOR PROGRAM---------------------------

import random
import string

#--->Function for Generating Random Password of length specified by user
def generatePass():
    str=(string.ascii_letters)+(string.digits)+(string.punctuation)
    password=""
    if pass_length==1:
        password+=random.choice(str)
    elif pass_length==2:
        str=(string.digits)+(string.punctuation)
        password+=random.choice(str)
        str=string.ascii_letters
        password+=random.choice(str)
    elif pass_length==3:
        str=string.digits
        password+=random.choice(str)
        str=string.ascii_letters
        password+=random.choice(str)
        str=string.punctuation
        password+=random.choice(str)
    elif pass_length>=4:
        if pass_length>4:
            for i in range(pass_length-4):
                password+=random.choice(str)
        str=string.digits
        password+=random.choice(str)
        str=string.ascii_lowercase
        password+=random.choice(str)
        str=string.ascii_uppercase
        password+=random.choice(str)
        str=string.punctuation
        password+=random.choice(str)
    return password
        
#--->Function for asking user if they want to generate another password
def ask():
    answer=input("Do you wish to Generate Password again (Y or N): ")
    answer.lower
    if answer=='n':
        print("EXITING...")
        exit()
    elif answer!='y':
        print("Invalid Input!")
        ask()
    else:
        return

#--->Program execution start from here
while True:
    pass_length=int(input("Enter the desired length for your Password: "))
    if pass_length>0:
        print(f"Your Password is: {generatePass()}")
    else:
        print("Length of the password should be a positive number!")
    ask()
