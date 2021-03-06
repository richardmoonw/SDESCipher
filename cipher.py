import re
import sys
from encryptor import transform
from attacker import brute_force

ENCRYPTION = "encryption"
DECRYPTION = "decryption"

def main():
    option_selected = "1"

    while option_selected != 0:
        print("##################################")
        print("#   WELCOME TO THE SDES CIPHER   #")
        print("#--------------------------------#")
        print("#                                #")
        print("# What do you wanna do?          #")
        print("# 1. Encrypt Something           #")
        print("# 2. Decrypt Something           #")
        print("# 0. Exit                        #")
        print("##################################\n")

        option_selected = input("Choose an option: ")

        if option_selected == "1":
            # Ask the user to type the 10 bits key and the 8 bits message to be encrypted.
            key = input("Please enter the 10 bit key to be used for encryption: ")
            message = input("Please enter the 8 bits message to be encrypted: ")

            output = transform(ENCRYPTION, key, message, True)
            print("Your message encrypted is {}\n".format(output))

        elif option_selected == "2":
            # Ask the user to type the 10 bits key and the 8 bits message to be decrypted.
            key = input("Please enter the 10 bit key to be used for decryption: ")
            message = input("Please enter the 8 bits message to be decrypted: ")

            output = transform(DECRYPTION, key, message, True)
            print("Your message decrypted is {}\n".format(output))
        elif option_selected == "0":
            exit(0)
        else:
            continue

if len(sys.argv) == 2:
    brute_force(sys.argv[1])
elif len(sys.argv) == 1:
    main()
else:
    print("Invalid number of arguments")