# A password generator is a useful tool that generates strong and
# random passwords for users. This project aims to create a
# password generator application using Python, allowing users to
# specify the length and complexity of the password.
# User Input: Prompt the user to specify the desired length of the
# password.
# Generate Password: Use a combination of random characters to
# generate a password of the specified length.
# Display the Password: Print the generated password on the screen.

import random
import string

def password_maker(n):
    char_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(char_set) for _ in range(n))
    return password

print("Welcome to the password generator!")
length = int(input("Enter the desired length of the password: "))
password = password_maker(length)
print("Generated Password:", password)

