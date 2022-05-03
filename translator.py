# Define your array (list) and give it some values
from tkinter import Y


acronyms = ['LOL', 'IDK', 'SMH']

# Display current values in the list
for acronym in acronyms:
    print(acronym)                      # Must be indented for it to work

user_input = input ("Would you like to add a new one? Y/N\n")
user_add = False

if user_input =="Y":
    user_add = True
else:
    user_add = False

#if user_add == True:
#    print("OK, let's add something")
#else:
#    print("Goodbye")

new_acronym = ""

if user_add == True:
    new_acronym = input ("WHat's your new acronym?\n")

if new_acronym in acronyms:
    print("That one's already there\n")
else:
    acronyms.append(new_acronym)
    print("Added '" + str(new_acronym) + "' to the list\n")

# Display current values in the list
for acronym in acronyms:
    print(acronym)                      # Must be indented for it to work