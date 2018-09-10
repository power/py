PlayerA = int(input("Pick a number between one and one hundred"))
PlayerB = int(input("Pick a number between one and one hundred"))
PlayerC = int(input("Pick a number between one and one hundred"))

if PlayerA == PlayerB:
    print ("This number has already been taken, PlayerB. Please pick another number")
    PlayerB = int(input("Pick a number between one and one hundred"))

if PlayerB == PlayerC:
    print ("This number has already been taken, PlayerC. Please pick another number")
    PlayerC = int(input("Pick a number between one and one hundred"))

if PlayerA == PlayerC:
    print ("This number has already been taken, PlayerC. Please pick another number")
    PlayerC = int(input("Pick a number between one and one hundred"))

print ("PlayerA's number is",PlayerA)
print ("PlayerB's number is",PlayerB)
print ("PlayerC's number is",PlayerC)

variable = 1
for count in range(1,100):
    variable = variable + 1
    list.append(variable)

list = []

list.append (PlayerA)
list.append (PlayerB)
list.append (PlayerC)


print (list)
