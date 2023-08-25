from math import pi
import random
from main import function_driver, print_colored


def your_name():
    n = input("Sun nimi: ")
    print(f"Hello, {n}!")


def area_of_circle_from_radius():
    r = float(input("Input the radius of the circle: "))
    print("The area of the circle is " + str(pi * r ** 2))


def area_of_rectangle():
    l = float(input("Input the length of the rectangle: "))
    w = float(input("Input the width of the rectangle: "))
    p = l * 2 + w * 2
    a = l * w
    print(f"The perimeter of the rectangle is {str(p)} and the area is {str(a)}")


def three_integers():
    i1 = int(input("Give me first integer: "))
    i2 = int(input("Give me second integer: "))
    i3 = int(input("Give me third integer: "))
    summ = i1 + i2 + i3
    product = i1 * i2 * i3
    average = summ / 3
    print(f"Sum {str(summ)}")
    print(f"Product {str(product)}")
    print(f"Average {str(average)}")


def medieval_to_modern():
    t = float(input("Enter talents: \n"))
    p = float(input("\nEnter pounds: \n"))
    l = float(input("\nEnter lots: \n"))
    total_grams = (t * 8512 + p * 425.6 + l * 13.5)
    grams = round(float(total_grams % 1000), 2)
    kg = int(total_grams // 1000)
    print(f"The weight in modern units \n{kg} kilograms and {grams} grams.")


def random_codes():
    three_digit = [random.randrange(0, 9) for i in range(3)]
    four_digit = [random.randrange(1, 6) for i in range(4)]
    print(f"3-digit code {three_digit}")
    print(f"4-digit code {four_digit}")
    # print(f"4-digit code {*four_digit}") <---- miksi ei toimi?
    # print(*four_digit)
    # print("4-digit code ", *four_digit) <---- ja tämä toimii?


if __name__ == "__main__":
    function_driver(__file__)
