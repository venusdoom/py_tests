# Guess game solver

print("Hello, my dear friend. Lets try to play my game.")
print("Enter a number in range of 1 to 100.")
print("The program will try to guess it and you should give an answer:")
print("     - if the number is correct type '1',")
print("     - if the number is greater type '2', ")
print("     - if the is lower type '3'.\n")

the_number = int(input("Your number is: "))
guess = 0

while guess != the_number:
    guess += 1
    print("Checking...", guess)

print("\nThe guess is:", guess, "\nYour number is:", the_number)

input("\nPress Enter to exit")
