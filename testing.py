# Define your array (list) and give it some values
acronyms = ['LOL', 'IDK', 'SMH']

# Display current values in the list
print(acronyms)

# Add some more values to the list
acronyms.append('BRB')
acronyms.append('TBH')
acronyms.append('BFN')
acronyms.append('IMHO')

print (acronyms)

# remove some values from the list
acronyms.remove('BFN')
# Display current values in the list
print(acronyms)
del acronyms[4]

# Display current values in the list
print(acronyms)


# Check to see if a value is in a list
if 1 in [1,2,3,4,5]:
    print('True')

# Define a new variable
word = 'BFN'

# Check to see if the new variable is in the original list
if word in acronyms:
    print (word + " is in the list")
else:
    print(word + " is NOT in the list")


# For loop
for acronym in acronyms:
    print(acronym)