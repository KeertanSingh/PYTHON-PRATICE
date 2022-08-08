


# Health Management System
# 3 clients
# total 6 files
# diet and exercise
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# *************************Let's Get Start***************************
import datetime


def getdate():
    current = datetime.datetime.now()
    return current.strftime("[%d-%m-%y || %I:%M]")


# print(getdate())

listName = ["keerat", "peter", "harry"]
def addData():
    name = input("""List of patient:
1. keerat
2. peter
3. harry
>>""")
    typeOfData = int(input(f"""What do you wanna add in {name} file:
Press "1" for diet
Press "2" for Exercise
>>>"""))
    if typeOfData == 1 and name in listName:
        dietAdd(name)
    elif typeOfData == 2 and name in listName:
        exerciseAdd(name)
    else:
        print("Invalid input")


# Adding the data
def dietAdd(name):
    meal = input("Enter the name of diet: ")
    with open(f"{name}Diet.txt", 'a') as file:
        file.write(f"{getdate()} ==> {meal}")


def exerciseAdd(name):
    exercise = input("Enter the name of exercise: ")
    with open(f"{name}ex.txt", 'a') as file:
        file.write(f"{getdate()} ==> {exercise}")


# retreive Data
def retreiveData():
    name = input("""List of patient:
1. keerat
2. peter
3. harry
>>""")
    typeOfData = int(input(f"""What do you wanna reterive from {name} file:
Press "1" for diet
Press "2" for Exercise
>>>"""))
    if typeOfData == 1 and name in listName:
        dietReterive(name)
    elif typeOfData == 2 and name in listName:
        exericseReterive(name)
    else:
        print(f"{name} is not listed")


def dietReterive(name):
    with open(f"{name}Diet.txt", 'r') as file:
        return file.read()


def exericseReterive(name):
    with open(f"{name}ex.txt", 'a') as file:
        return file.read()


if __name__ == '__main__':
    choice = int(input("""What do you want to do:
Press "1" for Add data
Press "2" for Retrieve data
>>>"""))
    if choice == 1:
        addData()
    elif choice == 2:
        retreiveData()
    else:
        print("Invalid input!!")
