# skill points test

print("You have 30 skill points.")
print("You can assign and unassign them into 4 characteristics: strength, health, wisdom and agility.")

skill_points = 30
CHARACTERISTICS = {"Strength": 0, "Health": 0, "Wisdom": 0, "Agility": 0}
user_choice = None
MENU_MAIN = """Main menu:
- enter 0 to exit
- enter 1 to assign a skill point to one of characteristics
- enter 2 to unassign a skill point from one of characteristics
"""
MENU_CHAR_ADD = """Characteristics menu:
- enter 1 to assign a skill point to Strength
- enter 2 to assign a skill point to Health
- enter 3 to assign a skill point to Wisdom
- enter 4 to assign a skill point to Agility
"""
MENU_CHAR_DEL = """Characteristics menu:
- enter 1 to unassign a skill point from Strength
- enter 2 to unassign a skill point from Health
- enter 3 to unassign a skill point from Wisdom
- enter 4 to unassign a skill point from Agility
"""

while user_choice != 0:
    print("Free skill points:", skill_points)
    print("Current characteristics", CHARACTERISTICS)
    print(MENU_MAIN)
    user_choice = input("Choose the option:")

    if user_choice == 1:
        print(MENU_CHAR_ADD)

