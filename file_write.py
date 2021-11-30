# f = open("sharan.txt","a")
# To write in file
# w for write
# a for append, it will join the content
# a = f.write("You are stupid, i hate you!")
# print(a)
# f.close()

# handle read and wrtie both
# f = open("sharan.txt","r+")
# print(f.read())
# f.write("keerat\n")
# f.write("joker\n")
# f.close()



# program to make file
print("let's make a file")
# name of file
name = input("what is name of file?\n")
# write file
f = open(name,"w")
type = input("What do you wanna type in it?\n")
f.write(type)
read = input("Do you wanna read you file?\nyes or no\n")
# read file
f=open(name,"r")
if read =="yes":
    print(f.read())
elif read == "no":
     print("Thanks You!!")
else:
    print("Something is wrong")
    # close file
f.close()