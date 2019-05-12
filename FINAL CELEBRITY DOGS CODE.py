
import sys
import random
error = ("You have entered an invalid option, please restart and try again.")
correct = ("Okay thank you")
blank = ("...")
victory = ("You win this round!")
defeat = ("You lose this round!")

print (30 * '-')
print ("   C E L E B R I T Y - D O G S")
print (30 * '-')
print ("1. START-GAME")
print ("2. LEAVE-GAME")
print (30 * '-')

select = int(input('Enter your choice [1-2]: '))


if select == 1:
    print("Starting Celebrity Dogs...")
elif select == 2:
    print("Closing Celebrity Dogs...")
    sys.exit()
else:
    print(error)
    sys.exit()


f = open("dogs.txt", "r")
dog_name =f.read()
dogs = dog_name.split('\n')

dogs_value = []



num_of_cards = int(input("Please enter the number of cards you would like to play with between 4 and 30\n"))
if num_of_cards < 4 :
    print (error)
    sys.exit
elif num_of_cards > 30:
    print (error)
    sys.exit
elif num_of_cards %2!= 0:
    print (error)
    sys.exit
else:
    print (correct)





for d in dogs:
    exercise = random.randint(1, 10)
    friendliness = random.randint(1, 100)
    intelligence = random.randint(1, 100)
    drool = random.randint (1, 10)
    dogs_value.append([d, exercise, friendliness, intelligence, drool])
random.shuffle (dogs_value)



f.close()
i = 0
player_deck = []
computer_deck = []
for i in range(0, num_of_cards):
    if i %2!= 0:
        player_deck.append(dogs_value[i])
    else:
        computer_deck.append(dogs_value[i])

print(player_deck)
print(blank)

c = []
i = 0
round = 0
while len(player_deck) > 0 and len(computer_deck) > 0 and round <= 60:
    round = (round + 1)
    player_card = player_deck.pop(0)
    computer_card = computer_deck.pop(0)
    print ("Your current card is", player_card)
    print("If excersise, friendliness or intelligence are selected then the highest value wins but if drool is selected then the lowest value wins.")
    category = int(input("Please enter a category: exercise=1, friendliness=2, intelligence=3 or drool=4."))
    print ("The computer's current card is", (computer_card))

    if category == (4):
        if player_card [category] <= computer_card [category]:
            print (victory)
            player_deck.append(player_card)
            player_deck.append(computer_card)
        elif player_card [category] > computer_card [category]:
            print (defeat)
            computer_deck.append(computer_card)
            computer_deck.append(player_card)
        else:
            sys.exit

    elif category == (1):
        if player_card [category] >= computer_card [category]:
            print (victory)
            player_deck.append(player_card)
            player_deck.append(computer_card)
        elif player_card [category] < computer_card [category]:
            print (defeat)
            computer_deck.append(computer_card)
            computer_deck.append(player_card)
        else:
            sys.exit

    elif category == (2):
        if player_card [category] >= computer_card [category]:
            print (victory)
            player_deck.append(player_card)
            player_deck.append(computer_card)
        elif player_card [category] < computer_card [category]:
            print (defeat)
            computer_deck.append(computer_card)
            computer_deck.append(player_card)
        else:
            sys.exit

    elif category == (3):
        if player_card [category] >= computer_card [category]:
            print (victory)
            player_deck.append(player_card)
            player_deck.append(computer_card)
        elif player_card [category] < computer_card [category]:
            print (defeat)
            computer_deck.append(computer_card)
            computer_deck.append(player_card)
        else:
            sys.exit


    else:
        print (error)

    print ("You have", (len(player_deck), "cards left"))

if len(player_deck) > 0:
    print ("YOU WIN!!!")
else:
    print ("Sorry you lose!!!")




