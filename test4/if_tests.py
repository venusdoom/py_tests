# testing if condition

import random

print("\nGuess the number\n")
number = int(input("Enter number from 1 to 10: "))
generator = random.randrange(10) + 1
if number == generator:
    print("You win! Entered number is", number, "and generated number is", generator)
    print("You are lucky person =)")
else:
    print("You lose! Entered number is", number, "and generated number is", generator)
    print("Maybe next time =)\n")

input("Press Enter to exit")
