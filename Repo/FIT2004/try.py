import math
number = 9.9
sroot = math.sqrt(number)
is_square = (number == int(sroot + 0.5) ** 2)
# check if number is a cube
croot = number**(1.0/3.0)
is_cube = (number == int(croot + 0.5) ** 3)
print(is_square)