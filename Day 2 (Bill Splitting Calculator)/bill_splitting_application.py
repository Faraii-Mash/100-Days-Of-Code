# By FB Mashiri for #100Days of Code
# A bill splitting app
# This program uses user input to combine to divide the bill by an input number of people including a tip by percentage 

# start the application with greeting
print('Welcome to an app that makes splitting the bill easier.')
# ask user to enter amount for bill
bill = float(input('What was the total bill? in $'))
# ask user to enter amount for tip as integer
tip = int(input('How much tip would you like to give? please insert percentage as number'))
# ask user the number of people who are sharing the bill
people = int(input('How many people to split the bill?'))

# convert tip to percentage
tip_as_percent = tip / 100
# calculate tip amount
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
# divide bill by number of people to pay
bill_per_person = total_bill / people
# round off final amount per person
final_amount = round(bill_per_person, 2)
# print the answer 
print(f"Each person should pay: ${final_amount}")