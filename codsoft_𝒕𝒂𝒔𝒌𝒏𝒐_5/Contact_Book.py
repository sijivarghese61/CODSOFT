#-------------------------------------Simple Contact Book Application-----------------------------------

#--->Creating a class 'Contact' to store all the details of a particular contact in an object.
class Contact:
    def __init__(self, name, number, email, address):
        self.name=name
        self.number=number
        self.email=email
        self.address=address
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.number}\nEmail: {self.email}\nAddress: {self.address}\n"

#--->Method for adding a new Contact.
def add():
    name=input("Enter Contact Name: ")
    number=input("Enter Phone Number: ")
    email=input("Enter Email: ")
    address=input("Enter Address: ")
    new=Contact(name, number, email, address)
    contacts.append(new)
    print(f"Contact {name} added successfully!")

#--->Method to view the details of the contact given by the user.
def view():
    if len(contacts)!=0:
        for i in contacts:
            print(f"Name: {i.name} -> Phone number: {i.number}")
    else:
        print("Oops! No contacts to show.\nTry adding a new contact.")

#--->Searching if a Contact entered by user is present or not, if found then printing it's details.
def search():
    term=input("Enter the name or phone number to search: ")
    found=0
    for i in contacts:
        if term==i.name or term==i.number:
            print(i)
            found=1
    if found==0:
        print(f"No contacts found with the search term '{term}'.")

#--->This Method is a sub part of updating user specified Contact. 
# It let the user to choose a specific detail of Contact they want to update.
def option():
    print("1. Name")
    print("2. Phone Number")
    print("3. Email")
    print("4. Address")
    opt=input("Choose the option number you want to update (1-4): ")
    return opt

#--->This Method is also a sub part of updating user specified Contact.
# Updation of Contact Detail takes place here.
def option_logic(contact,num):
    if num=='1':
        name=input(f"Enter the new name (current: {contact.name}): ")
        contact.name=name
    elif num=='2':
        number=input(f"Enter the new phone number (current: {contact.number}): ")
        contact.number=number
    elif num=='3':
        email=input(f"Enter the new email (current: {contact.email}): ")
        contact.email=email
    elif num=='4':
        address=input(f"Enter the new address (current: {contact.address}): ")
        contact.address=address
    else:
        print("Invalid option number! Try again with correct option number.")
        n= option()
        option_logic(contact,n)

#--->This is main Update Method which uses option() and option_logic() method to update the details.
def update():
    term=input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if term==contact.name or term==contact.number:
            while True:
                opt_num=option()
                option_logic(contact,opt_num)
                print(f"Contact {contact.name} updated successfully!")
                while True:
                    answer=input("Do you want to update any other details of {term} (Y or N): ")
                    answer.lower
                    if answer=='n':
                        return
                    elif answer=='y':
                        break
                    else:
                        print("Invalid Input!")
    print(f"No contacts found with the search term '{term}'.")

#--->Method for Deleting the user specified Contact.
def delete():
    term=input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if term==contact.name or term==contact.number:
            contacts.remove(contact)
            print(f"Contact {contact.name} deleted successfully!")
            return
    print(f"No contacts found with the search term '{term}'.")

#--->Method to show Menu options of Contact Book to user.
def menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

#--->Program execution starts from here
contacts = []
while True:
    menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        search()
    elif choice == '4':
        update()
    elif choice == '5':
        delete()
    elif choice == '6':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice! Please try again.")
