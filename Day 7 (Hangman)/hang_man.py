# By FB Mashiri for #100Days of Code
# This Program is a hangman game

#Game Start
import random

word_list_fn = 'words.txt'

def wordlist():
    #
    print('Hangman word list loading')
    #  inFile : open : read
    in_file = open(word_list_fn, 'r')
    # line to read
    line = in_file.readline()
    # word list Into list of string
    word_list = line.split()
    print(' ', len(word_list), 'words loaded')
    return word_list

def chosen_word(word_list):
    return random.choice(word_list)


word_list = wordlist()

def


