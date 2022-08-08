# Tuple and their function

# Mutable = Can Change
# Immutable = Can't  Change

# creating tuple
tp = (1, 2, 3)
# tp[1] = 4   #can't change the value in tuple
print(tp)

tup = (1,)    # Best way to create single value tuple
# tup = (1)   # This is not a tuple
print(tup)


# Exchange the value
a = 1
b = 2
a, b = b, a    # Exchanging the value 
print(a, b)