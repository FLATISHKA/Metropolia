import numpy as np


def rad_to_deg(radian):
    return np.rad2deg(radian)


def deg_to_rad(degree):
    return np.deg2rad(degree)


def display_conversion_table():
    degrees = np.arange(0, 361, 15)
    radians = np.deg2rad(degrees)
    print("-" * 20)
    for deg, rad in zip(degrees, radians):
        print(f"{deg}°\t ≈ {rad:.3f} rad")
    print("-" * 20)


def find_hypotenuse(leg1, leg2):
    return np.sqrt(leg1 ** 2 + leg2 ** 2)


def find_rectangle_sides(diagonal, ratio=(3, 2)):
    x = np.sqrt(diagonal ** 2 / (ratio[0] ** 2 + ratio[1] ** 2))
    return ratio[0] * x, ratio[1] * x


# 1.1
print(f"2.493 rad = {rad_to_deg(2.493):.2f}°")
print(f"0.911 rad = {rad_to_deg(0.911):.2f}°")

# 1.2
print(f"137.7° = {deg_to_rad(137.7):.4f} rad")
print(f"62.3° = {deg_to_rad(62.3):.4f} rad")

# 1.3
display_conversion_table()

# 2.1
print(f"Hypotenuse of the triangle is: {find_hypotenuse(1.6, 2.3):.2f} m")

# 2.3
sides = find_rectangle_sides(6.4)
print(f"Sides of the rectangle: {sides[0]:.2f}m and {sides[1]:.2f}m")