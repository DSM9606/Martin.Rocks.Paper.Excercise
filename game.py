# game.py

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("User Choice: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Valid. KEEP GOING")
else:
     print("INVALID PLAY AGAIN") 
     exit()





print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")