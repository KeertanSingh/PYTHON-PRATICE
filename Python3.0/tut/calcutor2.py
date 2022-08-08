def calculator(num1, num2, operator):
    # addition
    if operator == 1:
        print(f"Sum Of {num1} And {num2} = {num2 + num1}")

    # subtraction
    elif operator == 2:
        print(f"Difference Between {num1} And {num2} = {num1 - num2}")

    # multiplication
    elif operator == 3:
        print(f"Product Of {num1} And {num2} = {num1 * num2} ")

    # division
    elif operator == 4:
        print(f"Division Of {num1} And {num2} = {num1 / num2}")

    else:
        print("Something Is Wrong!")


if __name__ == '__main__':
    print("Welcome to advance calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = int(input("""What do you wanna do:
1. Addition     2. Subtraction      3. Multiplication       4. Division
>>"""))
    calculator(num1, num2, operator)
