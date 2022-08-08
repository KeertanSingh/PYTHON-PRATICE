# Variable = like a container

# Creating variable and storing data
var1 = "Hello world!!\n"  # string variable
var2 = 4  # integers
var3 = 34.5  # float
var4 = "keerat"

# printing the value of variable
print(var1)

# type
# printing the type of variable
print(type(var1))
# <class 'str'>
print(type(var2))
# <class 'int'>
print(type(var3))
# <class 'float'>


# Playing with variable
print(var2 + var3)  # It will add the value of variables
# print(var1 + var2)   #error because the we can't add integer and string together

# Concatenate the string
print(var1 + " " + var4)

# Datatype change
"""
int()
str()
float()
"""

num1 = "67"  # string
num2 = "123"  # string
num3 = 34  # integers
num4 = 45  # integers

print(num1 + num2)  # it will concatenate the string  not adding

# from string to integer
print(int(num1) + int(num2))  # It will add the variable now

# from integer to float
# before typecasting
print(num3 + num4)  # 79
# after the typecasting
print(float(num3) + float(num4))  # 79.0

# printing the number multiple time
print("Joker\n"*2)


# input function
number = input("Enter the number : ")     # It  will store the always as string , so we have to typecast if we want to add
print(int(number) + 45)



# quiz
# two number add  calcultor
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = number1+number2
print(f"Sum of {number1} and {number2} = {number3}")