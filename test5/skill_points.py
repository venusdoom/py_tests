# skill points test

print("You have 30 skill points.")
print("You can assign and unassign them into 4 characteristics: strength, health, wisdom and agility.")

skill_points = 30
CHARACTERISTICS = {"Strength": 0, "Health": 0, "Wisdom": 0, "Agility": 0}
user_choice = None
MENU = """Menu:
- enter 0 to exit
- enter 1 to assign skill point to Strength
- enter 2 to assign skill point to Health
"""

while user_choice != 0:
    print("Free skill points:", skill_points)
    print("Current characteristics", CHARACTERISTICS)
    print(MENU)