#keerat
# number of row
row = int(input("How many number of row do you want?\n"))
boolen = int(input("Type 1 or 0\n"))
pattern = bool(boolen)
i = 0
if pattern == True:
    while i < row:
        print("*"*(i+1))
        i = i +1

elif pattern == False:
    while row >=0:
        print("*"*(row))
        row = row-1
