# lambda function or anonymous function

# def add(a,b):
#     return a+b

# minus = lambda x, y: x - y
# add = lambda x, y: x + y
#
# print(minus(7, 4))
# print(add(7, 4))

def a_first(a):
    return a[1]


a = [[1, 14], [5, 6], [18, 23]]
# a.sort(key=a_first)
a.sort(key=lambda x: x[1])
print(a)
