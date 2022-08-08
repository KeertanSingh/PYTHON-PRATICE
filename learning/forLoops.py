# For loops in python

list1 = ["Spiderman", "Peter parker", "Keerat", "Joker"]  # Creating list
for item in list1:
    print(f"My name is {item}.")

dic1 = {
    "Harry": 1, "Keerat": 2
}
for key, value in dic1.items():
    print(f"{key} have {value} Phone.")

# Quiz
list2 = ["a", 11, 2, 3, 4, 12, 23, 134, "joker"]
for i in list2:
    if str(i).isnumeric() and i > 6:
        print(i)
    else:
        print("Not match")
