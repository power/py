userInput = input("Pick a fruit")
AnotherInput = input ("Pick another fruit")
userNumber = int(input("What position do you want your fruit to go in?"))
fruit = ["Apple", "Banana", "Strawberry", "Avocado", "Melon", "Apriocots", "Blackcurrant", "Cherry "]


item = 0
for count in fruit:
    print (fruit[item])
    item = item + 1


print (fruit)
fruit.insert(userNumber,AnotherInput)

fruit.remove("Banana")

fruit.append(userInput)

print (fruit)
