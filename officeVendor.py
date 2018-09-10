print ("-=+=--=+=--=+=--=+=--=+=--=+=--=+=-")
print ("            0    1    2            ")
print ("            3    4    5            ")
print ("            6    7    8            ")
print ("            /    9    #            ")
print ("-=+=--=+=--=+=--=+=--=+=--=+=--=+=-")



print ("If you would like to cancel your purchase please type cancel at any point")
end = input ("")

if end == "cancel":
    quit()

print ("Please input a number between 0 and 20.")
userInput = input("")

if userInput > "20":
    print ("Please input a number between 0 and 20.")
    newUserInput = input("")
while newUserInput > "20":
    print ("Please input a number between 0 and 20.")
    newUserInput = input("")

end = input ("At this point, you can either restart or cancel this. Type cancel or restart if you would.")
if end == "cancel":
    quit()

final = input ("Are you sure you would like to go through with your order?")
if final == "no":
    print ("The program will now end.")
    quit()

if userInput or newUserInput < "20":
    print ("Checking for your drink now.")

