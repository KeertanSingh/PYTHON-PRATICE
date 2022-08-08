class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def honor(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def biodata(self):
        return f"My name is {self.name}, I'm studying {self.major}, last year, I got {self.gpa} Percentage."


# objects
student1 = Student("Jim", "Business", 3.1)
student2 = Student("Peter", "Superhero", 7.3)

# acess information
print(student1.name)
print(student1.gpa)
print(student1.major)

print(student2.name)
print(student2.biodata())

print(student1.honor())
print(student2.honor())