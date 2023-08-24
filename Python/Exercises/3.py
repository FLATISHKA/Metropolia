from main import function_driver, print_colored


def zander_length_check():
    limit = 42
    print("A zander must be 42 centimeters or longer to meet the size limit.")
    zl = float(input("Whats the length of zander: "))
    if zl >= limit:
        print("Keep the fish.")
    else:
        print("Release the fish.")


def cabin_class_description():
    cc = input("Give me a class of your cabin: ").upper()
    if cc == "LUX":
        print("upper-deck cabin with a balcony.")
    elif cc == "A":
        print("above the car deck, equipped with a window.")
    elif cc == "B":
        print("windowless cabin above the car deck.")
    elif cc == "C":
        print("windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")


def hemoglobin_value():
    gender = input("Type your gender male/female: ").lower()
    hv = input("Whats your hemoglobin value: ")
    if(gender == "male"):
        if hv > 134 and hv < 167:
            print("You're ok")
        else:
            print("You dont have much time left...")
    elif(gender == "female"):
        if hv > 117 and hv < 155:
            print("You're ok")
        else:
            print("You dont have much time left...")
    else:
        print("Non existing gender, you should see a gender therapist...")


def leap_year_check():
    y = int(input("Enter any year AD: "))

    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print(f"{y} is a leap year!")
    else:
        print(f"{y} is a regular year without an extra day...")


try:
    function_driver(__file__)
except:
    print_colored("\nDriver error!", 31)
