#
# By FB Mashiri for #100Days of Code
# This Program is a silent option
from os import system
from art import logo
#  defining a function to clear the screen

def clear_screen():
    _ = system('clear')


def highest_bid(bid_dict):
    top_bid = 0
    winning_bid = ''
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
    if bid_amount > top_bid:
        top_bid = bid_amount
        winning_bid = bidder
    print(f'The winner is {winning_bid} with a bid of ${top_bid}')

bid_dict ={}
bidding_active = True

#  Start program
print(logo)

while bidding_active:
    print('Welcome to the silent auction')
    name = input('Please enter your name below\n')
    user_bid = int(input('Please enter the Bid amount below: \n$'))

    prog_continue = int(input("Are there any other bidders. Please enter:"
                          "1: Yes "
                          "2: No"))

    if prog_continue == 2:
        bidding_active = False
        highest_bid(bid_dict)
    elif prog_continue == 1:
        clear_screen()
    bid_dict[name] = user_bid

