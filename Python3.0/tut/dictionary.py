# Dictionary is used to store key, value pair 


# creating our first dictionary 
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# printing our dictionary
# print(monthConversions)

# accessing the value
print(monthConversions["Nov"])
print(monthConversions["Apr"])

# method of dictionary

# to get value by giving key
print(monthConversions.get("Mar"))
# if the key is not present in dictionary
print(monthConversions.get("lov", "Not a valid key"))
# will return all the keys
print(monthConversions.keys())
# Will return all the values
print(monthConversions.values())
# will return all the key and value
print(monthConversions.items())
# to copy whole dictionary
year = monthConversions.copy()
print(year)

dic = {
    "Keerat":"Hacker",
    "Aadi":"Businessman",
    "Joker":"Villian"
}
# print(dic)

# to update the dictionary
dic.update({"sharan":"Bhoot"})
# to remove specific key and value
dic.pop("Joker")
# print(dic)

# for loop in dictionary

for key, value in monthConversions.items():
    print(f"{key} full form is {value}")