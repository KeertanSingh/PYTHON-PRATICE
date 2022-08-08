# polymorphism

class Kali:

    def advantage(self):
        print("More Powerful")

    def disadvantage(self):
        print("Resource intensive")


class Parrot:
    def advantage(self):
        print("Lightweight")

    def disadvantage(self):
        print("Small community")


kali = Kali()
parrot = Parrot()

kali.advantage()
parrot.advantage()