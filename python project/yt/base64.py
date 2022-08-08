
import base64

def encoder(string):
    encoded = base64.b64encode(string)
    print(encoded)
    # pass

def decoder(string):
    pass

if __name__ == '__main__':
    print("Welcome to our base64 conveter")
    data_string = input("Enter your string here: ")
    data_byte = bytes(data_string, "utf-8")
    choose = input("""What do you want
1. encode
2. decode
>> """).lower()
    if choose == 'encode':
        encoder(data_byte)
    elif choose == 'decode':
        decoder(data_byte)
    else:
        print("invalid input")


def b64encode(string):
    return None