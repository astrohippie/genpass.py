Python Password Generator (genpass)

This is a Python script that generates strong passwords of length 12 by default. The password contains at least two digits and at least one special character. The user can also check the version of the script and exit the program.

Prerequisites

This script requires Python 3 to be installed on your system.

Usage:

To use the script, simply run it from the command line using the following command:

./genpass.py
python3 genpass.py

The script will display a welcome message and then prompt the user to select an option by entering a number.

Welcome to the Python Password Generator!
Select an option:
1. Generate password
2. Check version
3. Exit

To generate a new password, enter "1" at the prompt. The script will generate a strong password and display it on the screen.

To check the version of the script, enter "2" at the prompt. The script will display the version number and the name of the person who coded it.

To exit the program, enter "3" at the prompt.

Customization:

You can change the length of the generated password by modifying the pw_length parameter in the create_pw function.

python

def create_pw(pw_length=12):

You can also customize the characters used to generate the password by modifying the letters, digits, and special_chars variables in the create_pw function.

python

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

License:

This script is released under the MIT License.
