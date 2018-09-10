import random
import sys
def userMenu():
    print ("""
    1. Play Game
    2. Quit""")
    menuInput = input("")
    if menuInput == "Play" or "play":
        userGame()
    else:
        sys.exit()
def userGame():
    dogs = []
    cardCount = float(input("How many cards would you like to play with?"))
    if cardCount != 0:
        print("You need to pick an even number!")
        userMenu()
    if cardCount < 4:
        print ("You have entered too little cards. Please start again.")
        userMenu()
    if cardCount > 30:
        print ("You have entered too many cards. Please start again.")
        userMenu()
    f = open("dogs.txt", "r")
    for line in f:
        line = line.strip()
        print(dogs.append(line))
    print(dogs)
    
userMenu()
####################################### MENU ####################################### 
