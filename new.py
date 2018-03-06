# -------------------------------------------------------
# import library
import math

# -------------------------------------------------------
# calculate rect. square
height = 10
width = 20
rectangle_square = height * width
print("Площадь прямоугольника:", rectangle_square)

# -------------------------------------------------------
# calculate circle square
radius = 5
circle_square = math.pi * (radius**2)
print("Площадь круга:", round(circle_square, 2))
print(type(circle_square))

# -------------------------------------------------------
# calculate hypotenuse
catheter1 = 5
catheter2 = 6
hypotenuse = math.sqrt(catheter1**2 + catheter2**2)
print("Гипотенуза:", round(hypotenuse, 2))

