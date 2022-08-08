# Importing base64 module
import base64


def encoder(string):
    '''
    function for encoded the given string!
    '''
    encoded = base64.b64encode(string)  # Encoding the data
    print(f"""******************************
Output: {encoded.decode("utf-8")}
******************************""")  # Print the encoded data as string!


def decoder(string):
    '''
    function for decoded the given string!
    '''
    decoded = base64.b64decode(string)  # Decoding the data
    print(f"""******************************
Output: {decoded.decode("utf-8")}   
******************************""")  # Pring the decoded data as string.


if __name__ == '__main__':
    print("Welcome to base64 converter")
    data_string = input("Enter the string: ")  # Taking string
    data_byte = bytes(data_string, 'utf-8')  # Converting string into bytes
    choose = input("""What do you want:
1. encode
2. decode
>> """).lower()  # Asking user choose
    # Condition 
    if choose == "encode":
        encoder(data_byte)
    elif choose == "decode":
        decoder(data_byte)
    else:
        print("Invalid input.")
