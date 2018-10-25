# Write a password generator in Python. Be creative with how you generate passwords - strong passwords
# have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
# generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import string
import random

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(random.choice(string.punctuation))


def pass_generate(size= 8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


print(pass_generate(int(input('How many characters in your password?'))))