from main import function_driver
import random


def dice_roll_six():
    return random.randint(1, 6)


def dice_roll(dice_sides):
    return random.randint(1, dice_sides)


def gallons_to_litre_conversion(gallon):
    return gallon / 3.785

# ----------------------------------------


def dice_roll_until_six():
    dice = dice_roll_six()
    while dice < 6:
        print(f"you got: {dice}")
        dice = dice_roll_six()
    else:
        print(f"you got: {dice}!")


def dice_roll_until_modified():
    dice_sides = int(input(f"How many sides to the dice you want: "))
    dice = dice_roll(dice_sides)
    while dice < dice_sides:
        print(f"you got: {dice}")
        dice = dice_roll(dice_sides)
    else:
        print(f"you got: {dice}!")




exceptions = ["dice_roll", "dice_roll_six", "gallons_to_litre_conversion", "dice_roll_until_modified"]
function_driver(__file__, exceptions)
#dice_roll_until_six()
