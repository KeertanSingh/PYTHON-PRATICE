# Write file  in python

# write file
# with open("write", "w") as file:
with open("write", "a") as file:
    for i in range(1,11):
        # i = str(i)
        file.write(f"2 X {i} = {2 * i}\n")

# read file
with open("write") as r:
    content = r.read()
    print(content)
