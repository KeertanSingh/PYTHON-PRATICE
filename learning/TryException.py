# Try except exception handling

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
try:
    print(f"Sum: {int(num1) + int(num2)}")
except Exception as e:
    print(e)
print("This line is very important")
