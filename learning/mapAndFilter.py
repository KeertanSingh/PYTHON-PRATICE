# map(function, iterable )

def cube(num):
    return num ** 3


print(cube(3))

list1 = [1, 2, 3, 4, 5, 6, 7]
result = list(map(cube, list1))
print(result)


# filter(function, iterable )

def even(num):
    return num % 2 == 0


r2 = list(filter(even, list1))
print(r2)
