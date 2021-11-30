# This is math module

import math
from math import exp, expm1
x = 7.5
y = 5
a = -2
ex = 1.5e2
number = [1,2,3,4,5] #15
float = [0.1,0.2,0.3,0.4,0.5]#1.5

# Number-theoretic and representation functions
# 1.math.ceil(x)
# Return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float, delegates to x.__ceil__(), which should return an Integral value
print(math.ceil(x))
# print(x.__ceil__())
# output = 8

# 2. math.floor()
# Return the floor of x, the largest integer less than or equal to x. If x is not a float, delegates to x.__floor__(), which should return an Integral value.
print(math.floor(x))
# print(x.__floor__())
# output = 7

# 3. math.fsum(iterable)
# Return an accurate floating point sum of values in the iterable
print(math.fsum(number))
print(math.fsum(float))
# print(sum(number))
# print(sum(float))
# output = 5.0
# output = 1.5

# 4. math.copysign(x,y)
# Return a float with the magnitude(absolute value) of x but the sign of y.
print(math.copysign(y,a))
print(math.copysign(number[2],a))
# output = -5.0
# output = -3.0

# 5. math.fabs(x)
# Return the absolute value of x.
print(math.fabs(x))
print(math.fabs(y))
# output = 7.5
# output = 5.0

# 6. math.fmod(x,y)
# Return reminder of both number
print(math.fmod(x,y))
print(math.fmod(y,math.copysign(a,y)))
# output = 2.5
# output = 1.0

# 7. math.gcd(integers)
# Return the greatest common divisor of the specified integers
print(math.gcd(100))
# output = 100

# math.isclose
# print(math.isfinite())
# print(math.isqrt(y))
# math.comb()

# 8. math.lcm(intergers)
# Return lcm of numbers.
print(math.lcm(4,6,8))
# output = 24

# Power and logarithmic functions
# 1.math.exp(x)
# Return e raised to the power x, where e = 2.718281… is the base of natural logarithms.
print(math.exp(2))
# output = 7.38905609893065

# 2. math.pow()
# Return x raised to the power y
print(math.pow(5,2))
# output = 25.0

# 3.math.sqrt(x)
# Return the square root of x.
print(math.sqrt(144))
# output = 12.0
print(math.isqrt(143))
# output = 11
# when number has no perfect sqrt it chose lower number


# constants
# 1.math.pi
print(math.pi)
# The mathematical constant π = 3.141592…, to available precision.

#2. math.e
print(math.e)
# The mathematical constant e = 2.718281…, to available precision.



print("Calculator")
v1 = int(input("Enter first number here:\n"))
v2 = int(input("Enter second number here:\n"))
num = [v1,v2]
# num = []
# num.append(v1)
# num.append(v2)
print(type(num))
print(num)
print(math.fsum(num))