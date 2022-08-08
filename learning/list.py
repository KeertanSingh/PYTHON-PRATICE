# List and list function

# creating mixed list
grocery = ["Har-pic", "Vim bar", "DeoDurant", "Ladyfinger", 45]
print(grocery)  # printing all the value of list
print(grocery[3])  # printing the value which is at 3 index

# creating list
numbers = [1, 2, 43, 3, 4, 5, 6]
# numbers.sort()      # for ascending order
# numbers.reverse()   # to reverse the list
print(numbers)  # printing the all the value of list
print(numbers[3])  # printing value which is at 3 index

# list slicing
# print(numbers[0:4])
# print(numbers[0:])
# print(numbers[:7])
# print(numbers[:])
# print(numbers[::-1])
# print(numbers[::3])


# list function

# to get the length of list
print(len(numbers))
# to get the minimum value of list
print(min(numbers))
# to get the maximum value of list
print(max(numbers))

# it will add the value at last
numbers.append(90)
print(numbers)

# It will insert the value at index 2
numbers.insert(2, 45)
print(numbers)

# It will remove the value
numbers.remove(3)
print(numbers)

numbers.pop()  # will remove last value
numbers.pop(0)  # will remove the value from 0 index
print(numbers)

numbers[3] = 120  # will change the value of 3 index
print(numbers)
