import random                                   # Need to import the "random" function

#computer_choice = 'scissors'
computer_choice = random.choice(['rock', 'paper', 'scissors'])      # Allows variable to be set as a random from this array
user_choice = input("Do you want - rock, paper or scissors?\n")
winning_message = "You Win! The computer had " + computer_choice

if computer_choice == user_choice:
    print("Draw")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print (winning_message)
elif user_choice == 'paper' and computer_choice == 'rock':
    print (winning_message)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print (winning_message)
else:
    print("You lose :-( Computer wins with " + computer_choice)