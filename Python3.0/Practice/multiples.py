# to obtain a number and its 5 multiples

x = int(input("Enter the number: "))
print(f"X = {x}")
print("Its 5 multiples are: ")
for n in range(1, 6):
    print(f"{x} x {n} = {x*n}")
