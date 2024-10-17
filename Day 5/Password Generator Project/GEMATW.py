letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', " "]

print("Welcome to the PyPassword Generator!")

import random
import secrets
user_choice = int(input("Would you like to generate a password or check your password strength?\n"
                    "Type 1 to generate a password, Type 2 to encrypt a message\n"))

if user_choice == 1:
    length = int(input("Provide length of password?\n"))

    chars1 = letters + numbers + symbols
    password_list = []
    for l in range(length):
        if l == letters:
            password_list += secrets.choice(chars1)
        elif l == numbers:
            password_list += secrets.choice(chars1)
        elif l == symbols:
            password_list += secrets.choice(chars1)
        else:
            password_list += secrets.choice(chars1)
    random.shuffle(password_list)
    password = ""
    for l in password_list:
        password += l
    print(password)

    if user_choice == 1:
        user_option = input("Would you like to encrypt your password? Type Y for yes and N for No \n")
        if user_option == "Y":
            secret = chars1.copy()

            random.shuffle(secret)

            # print(f"chars: {chars1}")
            # print(f"encryption: {secret}")

            text = input("Input password to encrypt: \n")
            encrypt1 = ''

            for letter in text:
                index1 = chars1.index(letter)
                encrypt1 += secret[index1]

            print(f"original password: {text}")
            print(f"encrypted password: {encrypt1}")

            if user_option == "Y":
                user_option = input("Would you like to decrypt your password? Type Y for yes and N for No \n")
                if user_option == "Y":
                    password1 = input("Type encrypted password you would like to decrypt: \n")
                    decrypt1 = ''

                    for letter in password1:
                        index2 = secret.index(letter)
                        decrypt1 += chars1[index2]

                    print(f"encrypted password: {password1}")
                    print(f"original password: {decrypt1}")

                elif user_option == "N":
                    print("Thank you for your time!")

                else:
                    print("Wrong input! Try again!")

        elif user_choice == 2:
            print("Thank you for your time!")

        else:
            print("Wrong input! Please try again!")

elif user_choice == 2:
    chars2 = letters + numbers + symbols
    key = chars2.copy()

    random.shuffle(key)

    # print(f"chars: {chars2}")
    # print(f"keys: {key}")

    message1 = input("Enter a message to encrypt: \n")
    encrypt2 = ""

    for letter in message1:
        index2 = chars2.index(letter)
        encrypt2 += key[index2]

    print(f"original message: {message1}")
    print(f"encrypted message: {encrypt2}")

    if user_choice == 2:
        user_option = input("Would you like to decrypt your message? Type Y for yes and N for No \n")
        if user_option == "Y":
            message2 = input("Enter your encrypted message to decrypt: \n")
            decrypt2 = ''

            for letter in message2:
                index3 = key.index(letter)
                decrypt2 += chars2[index3]

            print(f"encrypted message: {message2}")
            # fix later
            print(f"original message: {decrypt2}")

        elif user_option == "N":
            print("Thank you for your time!")

        else:
            print("Wrong input! Try again!")
