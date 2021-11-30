car = {"Buggati":3000,"ferrari":2000,"india":{"punjab":1,"mumbai":2}}
# print(type(car))
# print(car)
# print(car["india"]["punjab"])
# car["sharan"]="Bhoot"
# del car["india"]
# item=car.copy()
# print(item.get("sharan"))
# item.update({"simu":"joker"})
# print(car)
# print(item)
# print(car.keys())
# print(car.items())


# dictionary functions?
name = {}
name.update({"sharan":"uncle","keerat":"cycly","khushi":"secretbox"})
# print(name.keys())
# print(name.values())
# print(name.get("sharan"))
# print(name.items())

#change value
# name["sharan"]="kumbkaran"

name["aya"]="nightmare"
name.pop("aya")

del name["khushi"]
# print(name)
# for x in name:
#     print(x)
#
# for x,y in name.items():
#     print(x,y)

# print(dict.fromkeys(name,car))

print("WELCOME TO MY DICTIONARY")
dic={"accord":"concurrence of opinion","evident":"clearly revealed to the mind or the senses or judgment",
     "practice":"a customary way of operation or behavior","intend":"have in ming as purpose"}
word=input("There are just 4 word:\n1.accord\n2.evident\n3.practice\n4.intend\nTo know the meaning of these word just type the word here\n")
print(word,"=",dic.get(word))