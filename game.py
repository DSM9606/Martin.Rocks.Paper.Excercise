# game.py
import random

print(" ")
print(" ")
print(" ")
print(" ")

print(" WELCOME TO Rock, Paper, Scissors, Shoot!")

print(" ")
print(" ")
print(" ")
print(" ")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors' : ")

print(" ")
print(" ")
print(" ")
print(" ")

print("User Choice: ", user_choice)

print(" ")
print(" ")
print(" ")
print(" ")

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("It looks like your choice,",user_choice,", is a valid choice!! SO LETS KEEP ON GOING!!")
else:
     print("INVALID CHOICE PLEASE PLAY AGAIN AND REMEMBER THE INPUTS ARE CASE SENSITIVE!!") 
     exit()

print(" ")
print(" ")
print(" ")
print(" ")

valid_options = ("rock", "paper", "scissors")
computer_choice = random.choice(valid_options)
print("Computer Choice: ", computer_choice)

# Notes
# because we are using the " or " operator in line 9 if any of the conditions are true the whole statement will be true
# if we use the " and " operator in line 9, ALL of the statements will need to be true to yield a true output
# one = sign means you are assigning a value
# two == signs mean that you are asking if one equals the other with a true or false output

print(" ")
print(" ")
print(" ")
print(" ")

if computer_choice == user_choice:
    print("It's a Tie!!, What a Coincidence!!")
elif computer_choice == "rock" and user_choice == "paper":
    print("Congratulations You Won!! , Paper Covers Rock!! ")
elif computer_choice == "rock" and user_choice == "scissors":
    print("OH NO THE COMPUTER WON THIS ROUND!! - Rock Crushes Scissors!!")
elif computer_choice == "paper" and user_choice == "rock":
    print("OH NO THE COMPUTER WON THIS ROUND!! -  Paper covers Rock")
elif computer_choice == "paper" and user_choice == "scissors":
    print("Congratulations You Won!! , Scissors cut Paper!! ")
elif computer_choice == "scissors" and user_choice == "paper":
    print("OH NO THE COMPUTER WON THIS ROUND!! - Scissors cut Paper!! " )
elif computer_choice == "scissors" and user_choice == "rock":
    print("Congratulations You Won!! , Rock Crushes Scissors!! ")

print(" ")
print(" ")
print(" ")
print(" ")

print("THIS IS THE END OF OUR GAME!! THANK YOU FOR PLAYING, PLEASE PLAY AGAIN!!")

print(" ")
print(" ")
print(" ")