# Dictionary and its function

# Creating dictionary
d = {"Peter": "Pizza", "spiderman": "panch", "keerat": {
    "breakfast": "roti",
    "lunch": "Sag"
}, "aadi": "Maggie"}

# Adding the key value in dic
d[34] = "Poha"
# printing the type of dic
# print(type(d))

print(d["Peter"])  # Printing the value of  peter
print(d["keerat"]['breakfast'])

del d["spiderman"]  # removing the spiderman

print(d)  # printing dic keys and value

# Dictionary method
dic = d.copy()  # copying the d
print(dic)

print(dic.get("keerat"))  # to get value of specific key

dic.update({"joban": "lollypop"})  # updating function
print(dic)

print(dic.keys())  # Return all the keys of dic

print(dic.items())  # Return all the item of dic

print(dic.values())  # Return all the values of dic
