# print text in reverse
print("This application is used for reversing user string and printing it.")

# initialising variables
word = input("\nEnter any word: ")
last_letter = len(word) - 1
reversed_word = ""

# going from last to first letter and creating new string
while last_letter != -1:
    reversed_word += word[last_letter]
    last_letter -= 1

print("Reversed word:", reversed_word)

input("\nPress Enter to exit.")
