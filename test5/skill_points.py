# skill points test

print("You have 10 skill points.")
print("You can assign and unassign them into 4 characteristics: strength, health, wisdom and agility.")

skill_points = 10
characteristics = {"Strength": 0, "Health": 0, "Wisdom": 0, "Agility": 0}
user_choice = None
char_choice = None
MENU_MAIN = """\nMain menu:
- enter 0 to exit
- enter 1 to assign a skill point to one of characteristics
- enter 2 to unassign a skill point from one of characteristics
"""
MENU_CHAR_ADD = """\nCharacteristics menu:
- enter 1 to assign a skill point to Strength
- enter 2 to assign a skill point to Health
- enter 3 to assign a skill point to Wisdom
- enter 4 to assign a skill point to Agility
"""
MENU_CHAR_DEL = """\nCharacteristics menu:
- enter 1 to unassign a skill point from Strength
- enter 2 to unassign a skill point from Health
- enter 3 to unassign a skill point from Wisdom
- enter 4 to unassign a skill point from Agility
"""

while user_choice != "0":
    print("\nFree skill points:", skill_points)
    print("Current characteristics", characteristics)
    print(MENU_MAIN)
    user_choice = input("Choose the option: ")
    if user_choice == "0":
        print("Good bye.")
    elif user_choice == "1":
        print(MENU_CHAR_ADD)
        char_choice = input("Choose the option: ")
        if skill_points == 0:
            print("No free SP.")
            print("You can unassign skill points from current characteristics.")
        elif char_choice == "1":
            characteristics["Strength"] += 1
            skill_points -= 1
        elif char_choice == "2":
            characteristics["Health"] += 1
            skill_points -= 1
        elif char_choice == "3":
            characteristics["Wisdom"] += 1
            skill_points -= 1
        elif char_choice == "4":
            characteristics["Agility"] += 1
            skill_points -= 1
        else:
            print("There is no such option.")
    elif user_choice == "2":
        print(MENU_CHAR_DEL)
        char_choice = input("Choose the option: ")
        if char_choice == "1" and characteristics["Strength"] != 0:
            characteristics["Strength"] -= 1
            skill_points += 1
        elif char_choice == "2" and characteristics["Health"] != 0:
            characteristics["Health"] -= 1
            skill_points += 1
        elif char_choice == "3" and characteristics["Wisdom"] != 0:
            characteristics["Wisdom"] -= 1
            skill_points += 1
        elif char_choice == "4" and characteristics["Agility"] != 0:
            characteristics["Agility"] -= 1
            skill_points += 1
        else:
            print("There is no such option, or there are 0 skill points in chosen characteristics.")
    else:
        print("There is no such option.")

input("\nPress Enter to exit.")
