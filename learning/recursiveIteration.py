def factorial_iterative(n):
    """Return the factorial of given number"""
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


# print(factorial_iterative.__doc__)


def factorial_recursive(n):
    """Return the factorial of given number"""
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120

number = int(input("Enter the number : "))
print(f"Factorial by iterative method: {factorial_iterative(number)}")
print(f"Factorial by recursive method: {factorial_recursive(number)}")


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Fibonacci : {fibonacci(number)}")
