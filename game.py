# game.py

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("User Choice: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Valid Choice My Friend. KEEP GOING!")
else:
     print("INVALID PLAY AGAIN") 
     exit()

# Notes
# because we are using the " or " operator in line 9 if any of the conditions are true the whole statement will be true
# if we use the " and " operator in line 9, ALL of the statements will need to be true to yield a true output
# one = sign means you are assigning a value
# two == signs mean that you are asking if one equals the other with a true or false output




print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")