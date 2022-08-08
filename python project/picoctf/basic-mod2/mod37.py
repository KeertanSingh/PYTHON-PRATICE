import string
with open("message.txt", "r") as f:
    content = f.read()
    numbers = content.splitlines()
    result = ""
    for number in numbers:
        number = int(number)
        mod = number % 37
        if mod <= 25:
            result = result + f"{string.ascii_uppercase[mod]}"
        elif 25 < mod <= 35:
            result = result + f"{string.digits[mod - 26]}"
        elif mod == 36:
            result = result + "_"

    with open("flag.txt", "w") as flag:
        flag.write("picoCTF{" + result + "}")
    # print("picoCTF{" + result + "}")

