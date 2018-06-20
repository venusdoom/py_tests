# try to find out who is the father
print("User enters a sons name and gets his fathers name.")

# creating dict
names_dict = {"Vanya": "Vasya", "Dima": "Gena", "Kolya": "Stepa"}
sons_name = None
fathers_name = None
choice = None
MENU = """\nMain menu:
1. exit
2. find out fathers name
3. add new pair of names
4. delete a pair of names
5. change fathers name of existing sons name
"""

# main loop
while choice != "1":
    print(MENU)
    choice = input("Enter an option from menu: ")
    if choice == "1":
        print("Good bye.")
    elif choice == "2":
        print("Current known names of sons:", names_dict.keys())
        sons_name = input("Enter a sons name: ")
        if sons_name in names_dict:
            print("His fathers name is:", names_dict[sons_name])
        else:
            print("There is no such name in dictionary.")
    elif choice == "3":
        sons_name = input("What name do you want to add: ")
        if sons_name in names_dict:
            print("Such name already exists in dictionary.")
        else:
            fathers_name = input("Enter his fathers name: ")
            names_dict[sons_name] = fathers_name
            print("New pair of names is added to dictionary.")
            print("Current dictionary:", names_dict)
    elif choice == "4":
        sons_name = input("What name do you want to delete?.\
                         \nIt will also delete his fathers name from dictionary: ")
        if sons_name in names_dict:
            del names_dict[sons_name]
            print("A pair of names is deleted from dictionary.")
            print("Current dictionary:", names_dict)
        else:
            print("There is no such name in dictionary.")
    elif choice == "5":
        sons_name = input("What name do you want to change: ")
        if sons_name in names_dict:
            fathers_name = input("Enter new fathers name for this sons name: ")
            names_dict[sons_name] = fathers_name
            print("A pair of names is changed in dictionary.")
            print("Current dictionary:", names_dict)
        else:
            print("There is no such name in dictionary.")

input("\nPress Enter to exit.")
