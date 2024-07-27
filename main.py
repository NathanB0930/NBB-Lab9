from decode import *
from encode import *

def encode(password):
    encoded = ""
    for i in password:
        num = int(i)
        num2 = (num + 3) % 10
        encoded += str(num2)
    return encoded


if __name__ == '__main__':
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    run = True
    encoded = ""
    decoded = ""
    while run:
        option = input("Please enter an option: ")
        if option == "1":
            try:
                password = input("Please enter your password to encode: ")
                encoded = encode(password)
                print("Your password has been encoded and stored!")
            except:
                print("Error: enter password again.")
        elif option == "2":
            try:
                decoded = decode(encoded)
                print("The encoded password is", encoded, "and the original passcode is", decoded,".")
            except:
                print("Error: enter password again.")
        elif option == "3":
            run = False

        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")