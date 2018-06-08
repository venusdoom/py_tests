# Guess game, hard mode

import random

print("Hello, my dear friend. Lets try to play my game.")
print("Try to guess randomly generated number in range of 1 to 100.")
print("The game will tell you if the guessed number is correct, or")
print("if the number is greater or lower than yours.")
print("You have only 7 tries.\n")

the_number = random.randint(1, 100)
guess = int(input("Your guess: "))
counter = 1

while counter < 8:
    if guess == the_number:
        print("The guessed number is correct.")
        break
    elif counter == 7:
        print("The guessed number is not correct. You have no more tries.")
        break
    elif guess > the_number:
        print("The number is lower than yours. Try again.")
        guess = int(input("Your guess: "))
        counter += 1
    elif guess < the_number:
        print("The number is greater than yours. Try again.")
        guess = int(input("Your guess: "))
        counter += 1

print("It took you", counter, "tries to guess the number.")

input("\nPress Enter to exit")
