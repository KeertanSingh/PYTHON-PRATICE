# Read file in python
file = open("joker")
content = file.read()
# content = file.readline()
# content = file.readlines()

# for i in content:
#     print(i)
content_list = content.splitlines()
print(content_list)
# print(content)
file.close()
