import random

roll = random.randint(1,6)

#print("Computer rolled a " + str(roll))

guess = int(input("Guess the dice roll:\n"))

#print("You guessed " + str(guess))
#print("Computer rolled " + str(roll))

if guess == roll:
    print("You guessed correctly, they rolled a " + str(roll))
else:
    print("You got it wrong, they rolled a " + str(roll))