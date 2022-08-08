with open("message.txt") as flip:
    contents = flip.read()

for i in range(0, len(contents), 3):
    chunk = contents[i:i + 3]

    #     # print(chunk)
    # het - the
    a, b, c = chunk
    print(c+a+b, end="")

