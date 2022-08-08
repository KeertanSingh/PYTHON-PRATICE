import string

#
# def inverse(n, mod):
#     for x in range(1, mod):
#         if (n * x) % mod == 1:
#             return x

result = ""
with open("msg.txt", "r") as f:
    content = f.read()
    numbers = content.split()

    # print(numbers)

    for number in numbers:

        number = int(number)
        # print(type(number), number)
        mode = pow(number, -1, 41)
        #     # print(mode)
        #
        if mode in range(1, 27):
            result = result + string.ascii_uppercase[mode-1]
        elif mode in range(27, 37):
            result = result + string.digits[mode - 27]
        else:
            result = result + "_"
    #
    print("picoCTF{"+result+"}")
