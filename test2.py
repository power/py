question5 = input ("Which animal is proven  to have the biggest ears? \n 1. Whale \n 2. African Elephant \n 3. Bat-eared fox \n 4. Fennec Fox \n Your answer: ")

while question5 == "hint":
    print ("This animal is usually very friendly with humans")
    question5 = input ("Which animal is proven  to have the biggest ears? \n 1. Whale \n 2. African Elephants \n 3. Bat-eared fox \n 4. Fennec Fox \n Your answer:")

if question2 == "African Elephant":
    score = score + 1
    print ("Correct, most people think it is the Bat-eared fox but they would be wrong.")
elif question2 != "African Elephant":
    score = score + 0
    print ("Ouch, not quite. The correct answer was the African Elephant.")
