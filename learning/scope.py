# scope, global variable


# l = 10  # Global variable
#
#
# def function1(n):
#     # l = 5  # Local variable
#     m = 8  # Local variable
#
#     global l
#     l = l + 3
#
#     print(l)
#     print(n, "i have printed")
#
#
# function1("This is me")
#
# print(l)
# # print(m)

x = 10


def harry():
    x = 20

    def rohan():
        global x
        x = 88

    print("Befor calling rohan ()", x)
    rohan()
    print("after rohan()", x)


harry()
print(x)
