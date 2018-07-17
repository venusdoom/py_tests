# a small game to test classes and objects


class Critter(object):
    """virtual pet"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        """Describes main attributes of Critter class"""
        description = "Object class Critter."
        description += "\nName: " + self.name + "\nMood: " + self.mood + "\nHunger: " + str(self.hunger) + "\nBoredom: " + str(self.boredom) + "\n"
        return description

    def __pass_time(self):
        """increase hunger and boredom level"""
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "great"
        elif 5 <= unhappiness <= 10:
            mood = "not bad"
        elif 10 <= unhappiness <= 15:
            mood = "not very well"
        else:
            mood = "bad"
        return mood

    def talk(self):
        print("My name is", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Mmm, thanks!\n")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("EEEaaaaa!\n")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Enter a name for new pet: ")
    crit = Critter(crit_name)

    # menu
    choice = None
    while choice != "0":
        print("""=My pet=
        0 - exit
        1 - talk with pet
        2 - feed pet
        3 - play with pet""")
        choice = input("Select an option from menu: ")
        if choice == "0":
            print("Bye!\n")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            try:
                food = int(input("How many food points do you want to give to the pet (enter a number): "))
            except ValueError as error:
                print("Input error:", error)
                print("Using default value for food (4).")
                food = 4
            crit.eat(food)
        elif choice == "3":
            try:
                fun = int(input("How many fun points do you want to give to the pet (enter a number): "))
            except ValueError as error:
                print("Input error:", error)
                print("Using default value for fun (4).")
                fun = 4
            crit.play(fun)
        elif choice == "4":
            print(crit)
        else:
            print("Sorry, there is no option:", choice, "\n")


main()
input("Press Enter to exit.")
