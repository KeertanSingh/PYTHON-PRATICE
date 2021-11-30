import random
#1. random.randint(a,b)
# for producing any random number at the range of a and b.
random_number = random.randint(1,10)
# print(random_number)

# 2.random.random()¶
# Return the next random floating point number in the range [0.0, 1.0).
rand = random.random() *100
# print(rand)

# 3.random.choice(seq)
# Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
list = ["code with harry", "Hackersploit", "Hackerspider1","tech cyber"]
choice = random.choice(list)
# print(choice)

# random.randrange(start, stop[, step])
# Return a randomly selected element from range(start, stop, step). This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
ran_range = random.randrange(0,5,2)
# print(ran_range)

# random.uniform(a, b)
# Return a random floating point number
ran_uniform = random.uniform(1,5)
print(ran_uniform)