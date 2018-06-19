# random word list
import random

print("This application is used to list words in random order.")

# creating and printing original words list
words_list = ["cat", "dog", "man", "home", "fly", "work", "light", "rain", "sun"]
print("Here is original words list:", words_list)

# printing all items randomly
print("Here is random list:")
while words_list:
    word = random.choice(words_list)
    print(word)
    words_list.remove(word)

input("\nPress Enter to exit.")
