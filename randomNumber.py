#myNumber.py
#This game uses a home made funiction
import random

#Think of a number
computer_number = random.randint(1,50)

print(computer_number)

#Create the function is_same()
def is_same (target, number):
    if target == number:
        result="Win"
    elif target > number:
        result="Low"
    else:
        result="High"
    return result

#Start the game
print ("Hello.\nI have thought of a number between 1 and 50.")

#Collect the user's guess as an integer
guess = int(input("Can you guess it?"))
#Use our function
higher_or_lower = is_same(computer_number, guess)
user_account = 0

#Run the game until the user is correct

while user_account < 5:
    user_account = user_account + 1
    while higher_or_lower != "Win":
        if higher_or_lower == "Low":
            guess = int(input("Sorry,you are too low. Try again."))
        print ("You have taken",user_account," amount of tries so far")
    while user_account > 6:
        print ("You failed to guess my number within  5 tries. The correct number was",computer_number,"Press RETURN to exit.")
    else:
        guess = int(input("Sorry, you are too high. Try again."))
        print ("You have taken",user_account," amount of tries so far")


    higher_or_lower = is_same(computer_number, guess)

#End the game
input ("Correct!\nWell done\n\n\nPress RETURN to exit.")
