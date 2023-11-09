import math

a_magnitude = 3.86
b_magnitude = 2.74
angle_degrees = 69.2

angle_radians = math.radians(angle_degrees)
print(angle_radians)

cos_theta = math.cos(angle_radians)
print(cos_theta)

sum_magnitude_squared = a_magnitude**2 + b_magnitude**2 + 2 * a_magnitude * b_magnitude * cos_theta
diff_magnitude_squared = a_magnitude**2 + b_magnitude**2 - 2 * a_magnitude * b_magnitude * cos_theta


sum_magnitude = math.sqrt(sum_magnitude_squared)
diff_magnitude = math.sqrt(diff_magnitude_squared)

print(sum_magnitude, diff_magnitude)
