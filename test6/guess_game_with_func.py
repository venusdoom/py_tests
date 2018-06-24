# Guess game, hard mode. With functions.

import random


def instruction():
    """Displays instruction."""
    print("Hello, my dear friend. Lets try to play my game.")
    print("Try to guess randomly generated number in range of 1 to 100.")
    print("The game will tell you if the guessed number is correct, or")
    print("if the number is greater or lower than yours.")
    print("You have only 7 tries.\n")


def ask_number(question, min, max, step=1):
    """Ask user to enter a number from min to max."""
    user_number = None
    while user_number not in range(min, max, step):
        user_number = int(input(question))
        if user_number not in range(min, max, step):
            print("The number is out of range (1-100).")
    return user_number


def random_number(min, max):
    """Generates random number in range of min to max."""
    random_number = random.randint(min, max)
    return random_number


def main():
    instruction()
    rand_numb = random_number(1, 100)
    user_numb = ask_number("Enter the number: ", 1, 100)
    counter = 1
    while counter < 8:
        if user_numb == rand_numb:
            print("The guessed number is correct.")
            break
        elif counter == 7:
            print("The guessed number is not correct. You have no more tries.")
            break
        elif user_numb > rand_numb:
            print("The number is lower than yours. Try again.")
            user_numb = ask_number("Enter the number: ", 1, 100)
            counter += 1
        elif user_numb < rand_numb:
            print("The number is greater than yours. Try again.")
            user_numb = ask_number("Enter the number: ", 1, 100)
            counter += 1
    print("It took you", counter, "tries to guess the number.")


# Launch the program.
main()

input("\nPress Enter to exit")
