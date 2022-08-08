# class and object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def biodatat(self):
        return f"My name is {self.name} and I'm {self.age}"



peter = Student("peter", 17)
joker = Student("joker", 18)

print(peter.name)
print(peter.age)
print(joker.age)
print(joker.biodatat())
print(peter.biodatat())