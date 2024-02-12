#task 1
import math

degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", radian)

#task 2

height = float(input("Height: "))
base1 = float(input("first value: "))
base2 = float(input("second value: "))

area = 0.5 * (base1 + base2) * height
print("Output:", area)


#task 3

import math

num_sides = int(input("num sides: "))
side_length = float(input("length of a side: "))

area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", area)


#task 4

base_length = float(input("length of base: "))
height_parallelogram = float(input("height of parallelogram: "))

area_parallelogram = base_length * height_parallelogram
print(" Output:", area_parallelogram)
