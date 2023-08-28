import random
from main import function_driver


def dice_roll():
    amount = int(input("How many dices would you like to roll: "))
    total = 0
    for dice in range(amount):
        dice_number = random.randint(1, 6)
        total = total + dice_number
        print(f"You got {dice_number}")
    print(f"sum of the all dices {total}")


def run_until_empty():
    numbers = []
    while True:
        number = input("Enter a number")
        if number == "":
            greatest = []
            sorted_numbers = sorted(numbers, reverse=True)
            for i, num in enumerate(sorted_numbers):
                if len(numbers) >= 5 and sorted_numbers[i] in sorted_numbers and i < 5:
                    greatest.append(sorted_numbers[i])
            print("Heres your five greatest numbers")
            print(greatest)
            break
        elif number.isnumeric():
            numbers.append(int(number))
            print("ok")
        else:
            print("THAT'S NOT A NUMBER!")


def is_prime_number():
    num = int(input("Give me some number of your choice: "))
    is_prime = False
    if num == 1:
        print("is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = True
                break
        if is_prime:
            print(f"{num} is not a prime number")
        else:
            print(f"{num} is a prime number")


def five_names_of_the_cities():
    mapping = ["first", "second", "third", "fourth", "fifth"]
    cities = []
    for i in range(5):
        city = input(f"Tell me {mapping[i]} name of the city: ")
        cities.append(city)
    for i, city in enumerate(cities):
        print(f"{mapping[i]} city was: {city}")

if __name__ == "__main__":
    function_driver(__file__)

