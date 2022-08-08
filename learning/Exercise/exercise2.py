# Faulty calculator
#  45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
try:
    number1 = int(input("Enter First Number : "))
    number2 = int(input("Enter Second Number : "))
    operator = input("""What do you wanna do:
    Press "+" for addition
    Press "-" for subtraction
    Press "*" for multiplication
    Press "/" for division
    >>""")

    if (number1 == 56 and number2 == 9 and operator == "+") or (number1 == 9 and number2 == 56 and operator == "+"):
        print(f"sum of {number1} and {number2} : 77")
    elif operator == "+":
        print(f"sum of {number1} and {number2} : { number1 + number2}")

    if (number1 == 43 and number2 == 3 and operator == "*") or (number1 == 3 and number2 == 43 and operator == "*"):
        print(f"Product of {number1} and {number2} = 555")

    elif operator == "*":
        print(f"Product  of {number1} and {number2} : {number1 * number2}")

    if  (number1 == 56 and number2 == 6 and operator == "/") or (number1 == 6 and number2 == 56 and operator == "/"):
        print(f"Product of {number1} and {number2} = 4")

    elif operator == "/":
        print(f"Division  of {number1} and {number2} : {number1 / number2}")
    elif operator == "-":
        print(f"Difference between {number1} and {number2} : {number1 - number2}")
except Exception as e:
    print(e)



