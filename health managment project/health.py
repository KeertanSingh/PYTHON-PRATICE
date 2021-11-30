# Health Management System
# This is a program to add or see the diet and exercise of clients.
# 3- clients = keerat, aya, aadi
# total file = 6
# 3 for diet
# 3 file for exercise



# let's start this new project
# Health management system
# to get and write date and time in programm import datetime module.
import datetime
def hospital():
    # ask what do you wanna do
    purpose = int(input("What do you wanna do?\nPress '1' for add data\nPress '2' for retrieve\n"))
    if purpose == 1:
        add_data()
    elif purpose == 2:
        retreive()

# function to add data in files
def add_data():
    type = int(input("What type of data you want to add?\npress 1 for diet\npress 2 for exercise\n"))

    if type == 1:
        diet_system()

    elif type == 2:
        exercise_system()

# function for add data in diet system
def diet_system():
    name = int(input("Whose data want you to add?\nPress 1 for keerat\nPress 2 for aya\nPressf 3 for aadi\n"))
    food = input("Enter food name here:\n")

    if name == 1:
        # writing file
        with open("fkeerat.txt","a") as a:
            a.write(str([str(datetime.datetime.now())]) + ":" + food + "\n")
            # a.write(food)
            print("successfuly written!!")

    elif name == 2:
        # writing file
        with open("faya.txt","a") as b:
            b.write(str([str(datetime.datetime.now())]) + ":" + food + "\n")
            print("successfuly written!!")

    elif name == 3:
        # writing file
        with open("faadi.txt","a") as c:
            c.write(str([str(datetime.datetime.now())]) + ":" + food + "\n")
            print("successfuly written!!")
    again()

# function to add exercise in file
def exercise_system():
    name = int(input("Whose data want you to add?\nPress 1 for keerat\nPress 2 for aya\nPress 3 for aadi\n"))
    exercise = input("Enter exercise name here:\n")
    if name == 1:
        # writing file
        with open("exkeerat.txt", "a") as a:
            a.write(str([str(datetime.datetime.now())]) + ":" + exercise + "\n")
            print("successfuly written!!")

    elif name == 2:
        # writing file
        with open("exaya.txt", "a") as b:
            b.write(str([str(datetime.datetime.now())]) + ":" + exercise + "\n")
            print("successfuly written!!")

    elif name == 3:
        # writing file
        with open("exaadi.txt", "a") as c:
            c.write(str([str(datetime.datetime.now())]) + ":" + exercise + "\n")
            print("successfuly written!!")
    again()

#function to get back data from files
def retreive():
    type = int(input("What type of data you want to retreive?\npress 1 for diet\npress 2 for exercise\n"))
    if type == 1:
        rdiet_system()

    elif type == 2:
        rexercise_system()

# function to get back data from diet system
def rdiet_system():
    name = int(input("Whose data want you to retreive?\nPress 1 for keerat\nPress 2 for aya\nPress 3 for aadi\n"))
    if name == 1:
        # reading file
        with open("fkeerat.txt") as a:
            print(a.read())


    elif name == 2:
        # reading file
        with open("faya.txt") as b:
            print(b.read())


    elif name == 3:
        # reading file
        with open("faadi.txt") as c:
            print(c.read())

    again()

# function to get back data from exercise system
def rexercise_system():
    name = int(input("Whose data want you to retreive?\nPress 1 for keerat\nPress 2 for aya\nPressf 3 for aadi\n"))

    if name == 1:
        # reading file
        with open("exkeerat.txt") as a:
            print(a.read())


    elif name == 2:
        # reading file
        with open("exaya.txt") as b:
            print(b.read())

    elif name == 3:
        # reading file
        with open("exaadi.txt") as c:
            print(c.read())

    again()

# function to run programm again
def again():
    again = input("Do you want to run programm again?\nyes or no\n")
    if again == "yes":
        hospital()
    elif again == "no":
        print("Thank You!!!")

hospital()