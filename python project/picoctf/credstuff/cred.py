# import alphabet
import alphabet as alphabet

with open("usernames.txt", "r") as f:
    users = f.read()
    users_list = users.split()

with open("passwords.txt", "r") as r:
    passwords = r.read()
    pass_list = passwords.split()


def cread(login):
    for user in users_list:
        if user == login:
            print(f"{user} = {pass_list[users_list.index(user)]}")



if __name__ == '__main__':
    user = input("Enter the name of the user: ")
    cread(user)
