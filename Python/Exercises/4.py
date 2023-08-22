from math import pi
import random


def thousand_numbers_divisible_by_three():
    i = 0
    while i <= 1000:
        if i % 3 == 0 and i !=0:
            print(i)
        i = i + 1


def convert_until_negative():
    while True:
        inches = float(input("Enter a value in inches (negative value to exit): "))
        if inches < 0:
            print("Exiting...")
            break
        else:
            centimeters = inches * 2.54
            print(f"{inches:.2f} inches is equal to {centimeters:.2f} centimeters.")


def run_until_empty():
    numbers = []
    while True:
        number = input("Enter a number (empty string to exit): ")
        if number == "":
            print(f"The smallest number you gave me was {min(numbers)} and the largest number was {max(numbers)}")
            print(numbers)
            break
        elif number.isnumeric():
            numbers.append(int(number))
            print("ok")
        else:
            print("THAT'S NOT A NUMBER!")


def guess_the_integer():
    i = random.randint(1, 10)
    print("Guess the number (Game)")
    while True:
        guess = int(input("type your guess: "))
        if guess == i:
            print("Corrent!")
            break
        elif guess < i:
            print("Too low")
        elif guess > i:
            print("too high")


def login():
    usr = "python"
    pwd = "rules"
    attempts = 5
    while True:
        if attempts <= 0:
            print("Access denied")
            break
        u = input("Username: ")
        p = input("Password: ")
        if (u == usr and p == pwd):
            print("Welcome!")
            break
        else:
            attempts = attempts - 1
            if attempts > 0:
                print(f"Attempts left: {attempts}/5")


try:
    thousand_numbers_divisible_by_three()
    convert_until_negative()
    run_until_empty()
    guess_the_integer()
    login()
except:
    print("Error!")