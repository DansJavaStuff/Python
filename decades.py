my_name = input ("What's your name?\n")
age = int(input("How old are you" + " " + my_name + "?\n"))      # input allows for user input, \n means enter input on new line
                                            # wrapping it in a int() will return the user input as an int
decades = age // 10                         # // will divide and return the whole number
years = age % 10                            # % will return the remainder
print (my_name + "You are " + str(decades) + " decades and " + str(years) + " years old.")