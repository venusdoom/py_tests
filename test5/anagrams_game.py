# anagrams game

import random

# creating tuple of words and selecting one of them
WORDS = ("game", "luck", "mistake", "winner", "house", "dinner", "mouse")
word = random.choice(WORDS)

# copying word to use it later for compare
correct = word

# creating empty anagram string
anagram = ""

# anagram creation
while word:
    position = random.randrange(len(word))
    anagram += word[position]
    word = word[:position] + word[(position+1):]

# game loop
print("Try to guess word. Anagram is:", anagram)
guess = input("Enter your guess (or nothing to exit the game): ")
while guess != correct and guess != "":
    guess = input("Not correct, try again: ")

if guess == correct:
    print("Congratulations! You win, it is correct word.")
    input("\nPress Enter to exit...")
else:
    input("\nYou've decided to exit. Press Enter...")
