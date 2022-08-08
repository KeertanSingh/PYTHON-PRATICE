# Args and kwargs

# def function_name_print(a, b, c, d):
#     print(a, b, c, d)

def funargs(student, *args, **kwargs):
    for item in args:
        print(student, item)
    for key, value in kwargs.items():
        print(f"{key} is {value}")

# function_name_print("keerat", "joker", "mj", "peter")

har = ["keerat", "joker", "mj", "peter", "hacker"]
normal = "I'm a"
kw = {"name":"joker", "hero": "yes"}
funargs(normal, *har, **kw)
