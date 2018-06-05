# testing random functions

import random

die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = die1 + die2

print("Die 1 =", die1, "Die 2 =", die2, "Total =", total)
input("Press Enter to exit")

