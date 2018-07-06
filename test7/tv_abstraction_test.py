# representing tv as a program object


class Telly(object):
    """tv as a program object"""

    def __init__(self, channel=0, volume=15):
        self.channel = channel
        self.volume = volume

    def select_channel(self):
        try:
            self.channel = int(input("\nPlease, select a channel number (0-30): "))
        except ValueError as error:
            print("\nThere is no such channel:", error)
            print("Selecting default channel.")
            self.channel = 0

        if self.channel > 30 or self.channel < 0:
            print("\nThere is no such channel:", self.channel)
            print("Selecting default channel.")
            self.channel = 0

    def higher_volume(self):
        self.volume += 1
        if self.volume > 30:
            self.volume = 30

    def lower_volume(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0

    def menu(self):
        print("\nYou now watching channel:", self.channel)
        print("Current volume level:", self.volume)
        print("""\n        TV menu:
        0 - turn off tv
        1 - select a channel
        2 - higher volume level
        3 - lower volume level\n""")


def main():
    tv = Telly()
    choice = None
    while choice != "0":
        tv.menu()
        choice = input("Select option from tv menu: ")
        if choice == "0":
            print("Turning tv off.")
        elif choice == "1":
            tv.select_channel()
        elif choice == "2":
            tv.higher_volume()
        elif choice == "3":
            tv.lower_volume()
        else:
            print("Unknown option:", choice)


main()
input("\nEnter Enter to exit.")
