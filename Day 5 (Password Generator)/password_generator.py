# By FB Mashiri for #100Days of Code
# This Program is a password generator
# This program uses user input to combine different inputs, loops, random module and string concatenation

#  Password Generator Starts Here
import random

#  Create Lists with Letters, Symbols and Numbers
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#  Print program start and ask user for inputs
print('Welcome to the Python Password Generator.')
num_letters_in = int(input('How many letters would you like in your password?\n'))
num_symbols_in = int(input(f'How many symbols would you like?\n'))
num_numbers_in = int(input(f'How many numbers would you like?\n'))

# Start Generator and build into a List
password_list = []

#  Random letters entry
for char in range(1, num_letters_in + 1):
    password_list.append(random.choice(letters))
#  Random symbols entry
for char in range(1, num_symbols_in + 1):
    password_list += random.choice(symbols)
#  Random numbers entry
for char in range(1, num_numbers_in + 1):
    password_list += random.choice(numbers)

#  Show compiled password
print(password_list)
# Shuffle and print password generated
random.shuffle(password_list)
print(password_list)

#  Compile the Password into a string
password = ''
for char in password_list:
    password += char

print(f'Your password is: {password}')

