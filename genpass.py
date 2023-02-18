#!/usr/bin/python3

import time
import secrets
import string


# Color codes for the welcome message
WELCOME_COLOR = '\033[1;35m'
SELECT_COLOR = '\033[1;34m'
RESET_COLOR = '\033[0m'


def create_pw(pw_length=12):
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   alphabet = letters + digits + special_chars
   pwd = ''
   pw_strong = False

   while not pw_strong:
       pwd = ''
       for i in range(pw_length):
           pwd += ''.join(secrets.choice(alphabet))

       if (any(char in special_chars for char in pwd) and
               sum(char in digits for char in pwd) >= 2):
           pw_strong = True

   return pwd


def select_option():
    while True:
        print(f"{SELECT_COLOR}Select an option:\n1. Generate password\n2. Check version\n3. Exit{RESET_COLOR}")
        option = input()
        if option == '1':
            print(f"{WELCOME_COLOR}New password generated: {RESET_COLOR}{create_pw()}")
        elif option == '2':
            print(f"{WELCOME_COLOR}Python password generator\nVersion 1.0\nCoded by: AstroHippie{RESET_COLOR}")
        elif option == '3':
            print(f"{WELCOME_COLOR}Exiting...{RESET_COLOR}")
            break
        else:
            print(f"{WELCOME_COLOR}Invalid option. Please try again.{RESET_COLOR}")


if __name__ == '__main__':
   print(f"{WELCOME_COLOR}Welcome to genpass, the Python Password Generator!{RESET_COLOR}")
   time.sleep(7)  # Sleep for 7 seconds
   select_option()
