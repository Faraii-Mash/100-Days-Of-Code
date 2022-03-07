# By FB Mashiri for #100Days of Code
# This Program is a cipher encryption & decryption tool
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
encrypted_text = ''
decrypted_text = ''
def greet_user(user_name):
    print(f'Hello {user_name}')
    print('Welcome to the Ceasers Cipher')
    print('This program can be use to encrypt and decrypt Ciphers')
    print('Please select an option below to work on a cipher:')


def cipher_option(user_option, user_word, shift_num):
    if user_option == 'decrypt':
        print(f'You have chosen to {user_option}')
        decryption_tool(user_word, shift_num)

    elif user_option == 'encrypt':
        print(f'You have chosen to {user_option}')
        encryption_tool(user_word, shift_num)

    else:
        print(f'You have chosen to {user_option}')
        print('You have entered an invalid option. Please try again')

def encryption_tool(user_word, shift_num):
    print(user_word)
    print(shift_num)
    for letter in user_word:
        encrypted_text = ''
        #  the letter position before shifting
        letter_pos_bef = alphabet.index(letter)
        letter_pos_aft = letter_pos_bef + shift_num
        encrypted_letter = alphabet[letter_pos_aft]
        encrypted_text += encrypted_letter

    print(f'The encrypted word is {encrypted_text}')

def decryption_tool(word, shift_num):
    print(word)
    print(shift_num)


user_name = input('Greetings, What is your name\n')
greet_user(user_name)
user_option = input('Would you like to encrypt or decrypt\n')

user_word = input('Please insert your word to decipher here:\n')
shift_num = int(input('How many shifts would you like to encode by:\n'))
cipher_option(user_option)
