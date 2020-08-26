import re
from encryptor import encrypt
from decryptor import decrypt

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
        print("# 3. Make a brute-force attack   #")
        print("# 0. Exit                        #")
        print("##################################\n")

        option_selected = input("Choose an option: ")

        if option_selected == "1":
            encrypt()
        elif option_selected == "2":
            decrypt()
        elif option_selected == "3":
            make_attack()
        elif option_selected == "0":
            exit(0)
        else:
            continue


def make_attack():
    return

main()