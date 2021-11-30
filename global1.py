# l = 10 # Global variable
#
#
#
# def function1(n):
#     # l = 5 # local variable
#     m = 9 # local variable
#     # to increase the value of global variable in function
#     global l
#     l = l + 15
#     print(l,m)
#     print(n,"I have printed.")
#
#
# function1("This is me,")
# print(l)
# print(m) # it defined in function

x = 89
def keerat():
    x = 20
    def aya():
        global x
        x = 10
    print("Before Calling rohan Aya()",x)
    aya()
    print("Afte Calling aya()",x)

keerat()
print(x)