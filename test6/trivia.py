# trivia game with customizable data


def instruction():
    """Displays instruction."""
    print("This is Trivia game.",
          "\nAnswer the questions and get scores.",
          "\nEasy - 1 point, Medium - 2 points, Hard - 3 points.")


def open_file(file_name, mode):
    """Opens selected text file in selected mode"""
    try:
        the_file = open(file_name, mode)
    except IOError as error:
        print("Cannot open game data file:", error)
        exit(1)
    else:
        return the_file


def read_blocks(the_file):
    """Reads blocks of game data"""
    theme = the_file.readline()
    difficulty = the_file.readline()
    question = the_file.readline()
    answers = []
    for answer in range(4):
        answers.append(the_file.readline())
    correct = the_file.readline()
    explanation = the_file.readline()
    return theme, difficulty, question, answers, correct, explanation


def scores(difficulty, score):
    """Calculates scores depending on difficulty"""
    if "Easy" in difficulty:
        score += 1
    elif "Medium" in difficulty:
        score += 2
    elif "Hard" in difficulty:
        score += 3
    return score


def ask_number(question, min, max, step=1):
    """Ask user to enter a number from min to max."""
    user_number = None
    while user_number not in range(min, max, step):
        try:
            user_number = int(input(question))
        except ValueError as error:
            print("Wrong input:", error)
            print("Please, enter a number in range of (1-4).")
        else:
            if user_number not in range(min, max, step):
                print("The number is out of range (1-4).")
    return user_number


def high_scores(user_name, score):
    """Creates high_scores list and writes it to file"""
    the_file = open_file("high_scores.txt", "a")
    h_scores_list = [user_name, "\t", str(score), "\n"]
    the_file.writelines(h_scores_list)
    the_file.close()


def main():
    instruction()
    game_data = open_file("game_data.txt", "r")
    score = 0

    # initialising first block
    theme, difficulty, question, answers, correct, explanation = read_blocks(game_data)

    while theme:
        print("\n", theme, difficulty, question, end=" ")
        for answer in answers:
            print(answer, end=" ")
        user_choice = ask_number("\nSelect the number of correct answer: ", 1, 5)
        if user_choice == int(correct):
            score = scores(difficulty, score)
            print("You right! The answer is correct.")
        else:
            print("The answer is not correct.")
        print(explanation, end=" ")
        print("\nYour score is:", score)

        # going to the next block
        theme, difficulty, question, answers, correct, explanation = read_blocks(game_data)

    game_data.close()
    print("That was the last question.")

    # set name for high scores table
    user_name = ""
    while len(user_name) == 0:
        user_name = input("\nEnter your name for high scores table: ")
        if user_name == "":
            print("User name should not be empty.")
    high_scores(user_name, score)


# launch the program.
main()

input("\nPress Enter to exit")
