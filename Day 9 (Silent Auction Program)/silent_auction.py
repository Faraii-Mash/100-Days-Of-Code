#
# By FB Mashiri for #100Days of Code
# This Program is a silent option
from os import system
from art import logo
#  defining a function to clear the screen

def clear_screen():
    _ = system('clear')

bid_dict ={}
bidding_active = True
#  Start program
print(logo)

while bidding_active:
    print('Welcome to the silent auction')
    name = input('Please enter your name below\n')
    user_bid = input('Please enter the Bid amount below: \n$')

    prog_continue = input("Are there any other bidders ")

bid_dict[name] = user_bid

