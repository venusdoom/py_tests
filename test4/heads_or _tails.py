# Heads or tails test

import random

print("The program simulates a coin toss for 100 times")
print("and tells you how many heads or tails there was.\n")

# init variables
counter = 0
tails = 0
heads = 0

# main cycle
while counter < 100:
    random_result = random.randint(1, 2)
    if random_result == 1:
        tails += 1
    else:
        heads += 1
    counter += 1

# printing results
print("Heads =", heads)
print("Tails =", tails)

# exit program
input("\nPress Enter to exit")


