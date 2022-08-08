# JSON module 

# Import the json module 
import json

"""
Notes:
JSON is a syntax for storing and exchanging data.
JSON is text, written with Javascript Object notation.
"""

# Parse JSON - Convert from JSON to Python 

# If you have JSON string, you can parse it by using the json.loads() method. 

# Some JSON Data
data = '{"name":"Peter", "age":18, "city":"New York"}'
print(data)  # we can't use dictionary functions because it is an string
# print(type(data))   #string

# Parse data 
parsed = json.loads(data)
print(parsed) # after parsing the data by json it become dictionary from string, so now we can use dictionary functions
# print(type(parsed))
# print(parsed["name"])


# dumps 
#Convert from Python to JSON

# If you have a python object, you can convert it into a JSON string by using the json.dumps() method.

# python object to javvascript compatible object 
data2 = {
    "channel":"hacktac",
    "cars": [1, 2, 3],
    "fridge":(120, "joker"),
    "isbad" :False

}
# print(data, type(data))

# convert into JSON:
iscomp  = json.dumps(data2)
# print(iscomp)

# Convert python objects into json string and print the values 
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None)) 

# sort_key used to sort the element into data 
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
