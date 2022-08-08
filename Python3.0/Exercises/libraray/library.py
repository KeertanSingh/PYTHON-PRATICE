class Library:

    def __init__(self, list, name):
        self.books_list = list
        self.name = name
        self.lenDict = {}

    def display_book(self, booklist):
        print(f"We have following books in our library: {self.name}")
        for book in self.books_list:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lenDict.keys():
            self.lenDict.update({book: user})
            print("Lender-book database has been updated. you can take the book now.")
        else:
            print(f"Book is already being lend by {self.lenDict[book]}")

    def add_book(self, book):
        self.books_list.append(book)
        print("Book has been added to the book list.")

    def return_book(self, book):
        self.lenDict.pop(book)


if __name__ == '__main__':

    keerat = Library(["python", "c++", "Github"], "Mahabharata")
    while True:
        print(f"Welcome to {keerat.name} library")
        user_choice = input("""What do you want to do:
1. Display book
2. Lend book
3. Add book
4. return book
>> """).lower()
        
        if user_choice == 'q':
            print("Thanks to visit in our library!!")
            break
        elif user_choice == "1":
            keerat.display_book(keerat.books_list)
        elif user_choice == "2":
            book = input("Enter the name of the book you want to lend: ")
            name = input("Enter your name: ")
            keerat.lend_book(name, book)
        elif user_choice == "3":
            book = input("Enter the name of book you want to add: ")
            keerat.add_book(book)
        elif user_choice == "4":
            book = input("Enter the name of book you want to return: ")
            keerat.return_book(book)
        else:
            print("Invalid input!!")

        print("Press 'q' to quite and 'c' to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
