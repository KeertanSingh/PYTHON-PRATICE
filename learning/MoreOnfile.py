f = open("test1")
# print(f.tell())   # pointer position
print(f.readline())
# print(f.tell())
f.seek(0)  # Reset the pointer
print(f.readline())
# print(f.tell())


f.close()
