from main import function_driver
from random import randint
from math import pi


class Exc:
    @staticmethod
    def dice_roll_six():
        return randint(1, 6)

    @staticmethod
    def dice_roll(sides):
        return randint(1, sides)

    @staticmethod
    def gal_to_litre(gal):
        return gal / 3.785

    @staticmethod
    def int_list_to_sum(numbers):
        summ = 0
        for num in numbers:
            summ = summ + num
        return summ

    @staticmethod
    def remove_uneven(numbers):
        even = []
        for num in numbers:
            if num % 2 == 0:
                even.append(num)
        return even

    @staticmethod
    def diameter_to_units_per_sq(diameter, price):
        radius = diameter / 2
        area = pi * radius ** 2
        unit_price = price / area
        return unit_price


def dice_roll_until_six():
    dice = Exc.dice_roll_six()
    while dice < 6:
        print(f"you got: {dice}")
        dice = Exc.dice_roll_six()
    else:
        print(f"you got: {dice}!")


def dice_roll_until_modified():
    dice_sides = int(input(f"How many sides for the dice you want: "))
    dice = Exc.dice_roll(dice_sides)
    while dice < dice_sides:
        print(f"you got: {dice}")
        dice = Exc.dice_roll(dice_sides)
    else:
        print(f"you got: {dice}!")


def gas_to_litre():
    while True:
        gallons = float(input("Enter a volume in gallons (negative to exit): "))
        if gallons < 0:
            break
        litres = Exc.gal_to_litre(gallons)
        print(f"{gallons} gallons is equal to {litres:.2f} litres.")


def sum_of_given_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers)
    print(Exc.int_list_to_sum(numbers))


def remove_uneven_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers)
    print(Exc.remove_uneven(numbers))


def pizza_price_in_sq():
    diameter = float(input("Enter a diameter of the pizza in cm: "))
    price = float(input("Enter a price fo the pizza: "))
    print(f"\nUnit Price for Pizza 1: {Exc.diameter_to_units_per_sq(diameter, price)} euros/square meter")


if __name__ == "__main__":
    function_driver(__file__)
