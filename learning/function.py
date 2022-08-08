# a = 9
# b = 8
# c = sum((a, b))
# print(c)


# Creating a function

# def fun1(a, b):
#     print("Hello you are in function 1", a+ b)
# fun1(4, 5)

def function2(a, b):
    """Docstring: This is function on average"""
    average = (a + b) / 2
    print(f"Average of {a} and {b} is {average}")
    # return "joker"


function2(10, 5)
print(function2.__doc__)  # printing docstring
