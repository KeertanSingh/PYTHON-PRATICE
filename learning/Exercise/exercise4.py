# Astrologer's Stars
# input = interger n
# boolean = 0, 1
# *
# **
# ***
# ****
"""
Name: keertan singh
Topic : Astrologer's star
"""
n = int(input("Enter the number of row: "))    # Taking number of row
pattern = bool(int(input("Chose 0 or 1: ")))     # boolean value for pattern
i = 1
f = open('star.txt', "w")     # Creating a file to write content
if pattern:
    """It will run when we Pattern = 1 or True"""
    f.write("Actual star\n")
    while i <= n:
        print("*" * i)
        f.write("*" * i+"\n")
        i += 1
else:
    """It will run when we Pattern = 0 or False"""
    f.write("Reverse Star\n")
    while i <= n:
        print("*" * n)
        f.write("*" * n+"\n")
        n -= 1
f.close()     # Closing the file
