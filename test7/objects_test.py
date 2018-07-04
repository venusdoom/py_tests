# a small game to test classes and objects


class Critter(object):
    """virtual pet"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

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
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Sorry, there is no option:", choice, "\n")


main()
input("Enter Enter to exit.")
