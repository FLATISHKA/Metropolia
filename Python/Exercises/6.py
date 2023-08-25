from main import function_driver
import random

class Exceptions:
    @staticmethod
    def dice_roll_six():
        return random.randint(1, 6)

    @staticmethod
    def dice_roll(dice_sides):
        return random.randint(1, dice_sides)

    @staticmethod
    def gallons_to_litre_conversion(gallon):
        return gallon / 3.785


def dice_roll_until_six():
    dice = Exceptions.dice_roll_six()
    while dice < 6:
        print(f"you got: {dice}")
        dice = Exceptions.dice_roll_six()
    else:
        print(f"you got: {dice}!")


def dice_roll_until_modified():
    dice_sides = int(input(f"How many sides to the dice you want: "))
    dice = Exceptions.dice_roll(dice_sides)
    while dice < dice_sides:
        print(f"you got: {dice}")
        dice = Exceptions.dice_roll(dice_sides)
    else:
        print(f"you got: {dice}!")




if __name__ == "__main__":
    function_driver(__file__)