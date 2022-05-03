#temperature = 95
#if temperature > 80:
#    print("It's too hot!")
#    print("Stay inside!")
#elif temperature < 60:
#    print("It's too cold!")
#    print ("Stay inside!")
#else:
#    print ("Enjoy the outdoors!")
#print("Have a good day!")

#########################################################

#temperature = 95
#forecast = "rain"
#
#if temperature > 80 or temperature < 60:           # OR statement, either of the comparisons need to be true for the whole to evaluate as true
#    print("Stay inside!")
#else:
#    print("Enjoy the outdoors!")

#########################################################

#temperature = 75
#forecast = "sunny"
#
#if temperature < 80 and forecast !="rain":         # AND statement, both comparisons need to be true for the whole to evaluate as true
#    print("Go outside!")
#else:
#    print("Stay inside!")

#########################################################

#temperature = 75
#forecast = "rain"
#
#if not forecast == "rain":                    # NOT statement, checks to see if something insn't true
#    print("Go outside!")
#else:
#    print("Stay inside!")

#########################################################

raining = True
if raining:
    print("Stay inside!")

if not raining:
    print ("Go outside!")
else:
    print("Stay indoors!")