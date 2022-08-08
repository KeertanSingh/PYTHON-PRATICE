# string and their method

# creating string
mystr = "I'm spiderman"
str = "peterparker"
print(mystr)  # printing value of mystr
print(mystr[5])  # can print just one piece
print(mystr[4:13])  # printing part of string
print(len(mystr))  # len() function to get the full length of variable
print(mystr[0:13:2])  # printing the string, and it will skip 1 value everytime
# print(mystr[:13])     #equal to [0:13]
# print(mystr[0:])     #equal to [0:13]
# print(mystr[:])     #equal to [0:13]
# print(mystr[::])     #equal to [0:13:1]
print(mystr[-4:])
print(mystr[::-1])  # reverse th string
print(mystr[::-2])  # reverse th string , then skiping one letter

# string method
print(str.isalnum())  # tell us whether string is alpahnum or not, without spaces
print(str.isalpha())
print(str.endswith("kar"))
print(str.count("p"))
print(str.capitalize())
print(str.find("kar"))
print(str.lower())
print(str.upper())
print(str.replace("peter", "spiderman"))  # temporary change
print(str)
