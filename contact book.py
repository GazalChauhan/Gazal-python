
#python code for contact book
contact = {}


def display_contact():
    print("Name\t\tContact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
        
# asking choice of user
while True:
    choice = int(input ("1. Add new contact \n 2. Search contact \n 3. Display contact\n 4. Edit contact \n 5. Delete contact\n 6. Exit\n enter your choice"))
    if choice == 1:
        name = input("enter the contact name")
        phone = input("enter the mobile number")
        contact[name] = phone
    elif choice == 2:
        search_name = input("enter the cintact name ")
        if search_name in contact:
            print(search_name,"s contact number is",contact[search_name])
        else:
            print("name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("enter the contact to be edited")
        if edit_contact in contact:
            phone = input("enter mobile number")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("name is not found in contact book")
    elif choice == 5:
        del_contact = input("enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("do you want to delete the contact ")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact()
        else:
              print("name is not found in contact book")   
    else:
        break    
            

