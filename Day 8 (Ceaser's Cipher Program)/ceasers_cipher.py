# By FB Mashiri for #100Days of Code
# This Program is a cipher encryption & decryption tool

def greet_user(user_name):
    print(f'Hello {user_name}')
    print('Welcome to the Ceasers Cipher')
    print('This program can be use to encrypt and decrypt Ciphers')
    print('Please select an option below to work on a cipher:')


def cipher_option(user_option):
    if user_option == 'decrypt':
        print(f'You have chosen to {user_option}')

    elif user_option == 'encrypt':
        print(f'You have chosen to {user_option}')

    else:
        print(f'You have chosen to {user_option}')
        print('You have entered an invalid option. Please try again')


def encryption_tool(word,shift_num):
    print(word)
    print(shift_num)


def decryption_tool(word,shift_num):
    print(word)
    print(shift_num)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

user_name = input('Greetings, What is your name\n')
greet_user(user_name)
user_option = input('Would you like to encrypt or decrypt\n')
cipher_option(user_option)
shift_num = input('How many shifts would you like to encode by:\n')

