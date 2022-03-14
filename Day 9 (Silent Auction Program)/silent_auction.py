#
# By FB Mashiri for #100Days of Code
# This Program is a silent option

#  defining a function to clear the screen
new_dictionary = {"Day": "Monday",
                  "Week": "Week 2",
                  "Year": "2022"}

print(f'This is printing out of a dictionary'
      f'The Day is  {new_dictionary["Day"]}\n'
      f'In the {new_dictionary["Week"]}\n'
      f'This is the year {new_dictionary["Year"]}\n')

new_dictionary["Week"] = "Week 4 is the new entry"
#create a new dictionary
dict1 = {}

print(new_dictionary)
print(dict1)

for things in new_dictionary:
    print(things)
    print(new_dictionary[things])