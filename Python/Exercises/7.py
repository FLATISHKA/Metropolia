from main import function_driver


def corresponding_season():
    seasons = ("summer", "autumn", "winter", "spring")
    mapping = {0: 2, 1: 2, 2: 3, 3: 3, 4: 3, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1, 10: 1, 11: 2}
    month = int(input("Enter a number of a month: "))
    print(f"corresponding season to the month by number {month} is {seasons[mapping[month]]}")


def tuple_names():
    names = ()
    while True:
        name = input("Enter a name: ")
        if name == "":

            break
        elif name in names:
            print("Existing name")
        else:
            print("New name")
            names = (*names, name)
    for name in names:
        print(name)


def airports():
    airs = {}
    while True:
        ans = input(
            "Would you like to enter a new airport,\n fetch the information of an existing airport or quit ( E/F/Q ):").upper()
        if (ans == "Q"):
            break
        elif (ans == "E"):
            name = input("Enter an airport name:")
            code = input("Enter an airports ICAO code: ")
            airs[code] = name
        elif (ans == "F"):
            code = input("Enter an airports ICAO code: ")
            print(f"Airport name: {airs[code]}")


if __name__ == "__main__":
    function_driver(__file__)
