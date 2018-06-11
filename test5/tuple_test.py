# testing tuple

# creating tuple
inventory = ("sword", "shield", "dagger", "potion")

# printing list of items in tuple
print("Your inventory:", inventory)

# checking how many items in tuple
print("It consists of", len(inventory), "items.")

# listing items in tuple using "for"
print("\nList of the items using 'for':")
for item in inventory:
    print(item)

# checking indexes in tuple
index = int(input("\nEnter index number of one item: "))
print("Index", index, "stands for", inventory[index])

# checking slices in tuple
start = int(input("\nEnter first index: "))
stop = int(input("Enter last index: "))
print("Items between indexes:", inventory[start:stop])

# checking if the item exists in tuple
search = input("\nEnter a name of some item, to check if it exists in inventory: ")
if search in inventory:
    print(search.title(), "is in inventory.")
else:
    print(search.title(), "is not in inventory.")

# adding one tuple to another
chest = ("vine", "rum", "vodka")
print("\nYou've opened the chest and there are some new items in inventory:", inventory + chest)

# adding one tuple to another, second edition
inventory += chest
print("\nAnother try:", inventory)

input("\nPress Enter to exit")
