import sys 
import random

def userMenu():
    menuInput = input("""
    Welcome to Dog Trumps!
        Please select an option
        1. Play
        2. Quit""").lower()

        if menuInput == "play":
            userGame():
        elif menuInput == "quit":
            print("Thanks for playing! Exiting...")
            sys.exit()
        else:
            print ("Invalid response, please try again.")
            userMenu()

def userGame():
    userdognames =[],[],[],[],[]
    cpudognames =[],[],[],[],[]
    cardAmount = int(input("How many cards would you like to play with?"))
    
    if cardAmount >31 or cardAmount <3 or cardAmount % 2 != 0:
        print("""You selected an invalid number, it must fit the following criteria
            •Be equal to 4 or above
            •Be equal to 30 or lower
            •Be a whole, even number""" )
        userGame()
    usercards=int(cardAmount/2)
    cpucards=int(cardAmount/2)
    u = random.randint(0,cpucards)
    f = open("dogs.txt", "r")
    lines = f.read.()splitlines()
    for i in range (usercards):
        userdognames[0].append(random.choice(lines))
        userdognames[1].append(random.randint(1,5))
        userdognames[2].append(random.randint(1,100))
        userdognames[3].append(random.randint(1,10))
        userdognames[4].append(random.randint(1,10))
    for i in range(usercards):
        cpudognames[0].append(random.choice(lines))
        cpudognames[1].append(random.randint(1,5))
        cpudognames[2].append(random.randint(1,100))
        cpudognames[3].append(random.randint(1,10))
        cpudognames[4].append(random.randint(1,10))

    while len(cpudognames[0]) > 0 or len(userdognames[0]) > 0:
        print(""" This is your top card:
        """,userdognames[0][0],
        """Exercise:""",userdognames[1][0]"""/5"""
        """Intelligence:""", userdognames[2][0],"""/100"""
        """Friendliness:""", userdognames[3][0],"""/10"""
        """Drool:""", userdognames[4][0],"""/10""")

        stat = input("\n Please pick an ability").lower()

        if stat == ("exercise"):
            e = 1
        elif stat == ("intelligence"):
            e = 2
        elif stat == ("friendliness"):
            e = 3
        elif stat == ("drool"):
            e = 4

        print("You chose",userdognames[0][0]," and the ability ",stat,":",userdognames[e][0])
        print("\n\nThe computer has chosen\n",cpudognames[0][0],"\nand its",stat,"stat is:",cpudognames[e][0])
                    userscore = userdognames[e][p]
                    cpuscore = cpudognames[e][p]
                    if stat == ("drool"):
                        if userscore > cpuscore:
                            print("You Lose! The computer gets your card.")
                            for n in range(5):
                                move = userdognames[n][0]
                                del userdognames[n][0]
                                cpudognames[n].append(move)
                                cpumove = cpudognames[n][0]
                                del cpudognames[n][0]
                                cpudognames[n].append(cpumove)
                        if userscore <= cpuscore:
                            print("You Win! Well Done! You get both of the cards shuffled to the back of your deck.")
                            for n in range(5):
                                move = userdognames[n][0]
                                del userdognames[n][0]
                                userdognames[n].append(move)
                                cpumove = cpudognames[n][0]
                                del cpudognames[n][0]
                                userdognames[n].append(cpumove)
                    else:

                        if userscore >= cpuscore:
                            print("\nYou win! Well Done! You get both of the cards shuffled to the back of your deck.")
                            for n in range(5):
                                move = userdognames[n][0]
                                del userdognames[n][0]
                                userdognames[n].append(move)
                                cpumove = cpudognames[n][0]
                                del cpudognames[n][0]
                                userdognames[n].append(cpumove)                           
                        if userscore < cpuscore:
                            print("\nYou Lose! The computer gets your card.")
                            for n in range(5):
                                move = userdognames[n][0]
                                del userdognames[n][0]
                                cpudognames[n].append(move)
                                cpumove = cpudognames[n][0]
                                del cpudognames[n][0]
                                cpudognames[n].append(cpumove)
                    if len(userdognames[0]) == "0":
                        print("\nYou lose to the computer, better luck next time...")
                    if len(cpudognames[0]) == "0":
                        print("\nYou win against the computer, Well Done!\n")
                    userlistlength = str(len(userdognames[0]))
                    cpulistlength = str(len(cpudognames[0]))
                    print("\nyou have",userlistlength,"cards, the computer has",cpulistlength,"cards.\n")
