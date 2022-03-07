# By FB Mashiri for #100Days of Code
# This Program is a cipher encryption & decryption tool

def greet_user(user_name):
    print(f'Hello {user_name}')
    print('Welcome to the Ceasers Cipher')
    print('This program can be use to encrypt and decrypt Ciphers')
    print('Please select an option below to work on a cipher:')


def cipher_option(option):
    print('print')

user_name = input('Greetings, What is your name\n')
greet_user(user_name)


option = input('Would you like to encrypt or decrypt\n')


if user_option == 'decrypt':
    print('decrypt')

elif user_option == 'encrypt':
    print('encrypt')

else:
    print('You have entered an invalid option. Please try again')