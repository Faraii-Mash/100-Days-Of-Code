# By FB Mashiri for #100Days of Code
# A simple rock paper scissors application
# This program uses user input to combine to divide the bill by an input number of people including a tip by percentage
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#  Rock Paper Scissors Program
print('Welcome to the Rock Paper Scissors application')
choice_pics = [rock, paper, scissors]

user_in = int(input('Select either 0 for Rock, 1 for paper or 2 for Scissors. \n'))

if user_in >= 3 or user_in < 0:
    print('The number selected is an invalid input. Re-run the program and select 0,1 or 2')
else:
    print('You chose: ')
    print(choice_pics[user_in])

    comp_in = random.randint(0, 2)
    print('The computer chose: ')
    print(choice_pics[comp_in])

    #  User rock over comp Scissors
    if user_in == 0 and comp_in == 2:
        print('YOU WIN!')
    #  Comp Scissors over User rock
    elif user_in == 2 and comp_in == 0:
        print('YOU LOSE!')

    elif user_in > comp_in:
        print('YOU WIN!')

    elif user_in < comp_in:
        print('YOU LOSE!')

    elif user_in == comp_in:
        print('It is a Draw!')
