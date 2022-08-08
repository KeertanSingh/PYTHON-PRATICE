# Break and continue
# i = 0
# while (True):
#     if i + 1 < 5:
#         i = i + 1
#         continue
#     print(i, end=" ")
#
#     if i == 45:
#         break
#     i = i + 1


# Quiz

while True:
    n = int(input("Enter the number: "))
    if n <= 100:
        print("Try again!")
        continue
    else:
        print("You have choose greater number than 100.")
        break
