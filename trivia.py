score = 0
name = input ("What is your name?")
print ("Hello and welcome to my 10 question trivia quiz",name,"\n The rules of this game are as follows:\n \u2022 You will be shown a question with 4 answers, you are required to type the answer and not the number shown\n \u2022 You will be given a score out of 10 marks, 1 per question \n \u2022 If you need a hint, you are able to use them by typing 'hint' and a hint will be displayed \n \u2002 Apart from that, good luck and have fun.")
ready = input ("Are you ready?")

question1 = input ("What is the capital of china?\n 1. Bangkok\n 2. Beijing \n 3. Washington DC \n 4. Shanghai \n Your answer: ")


if question1 == "hint":
    print ("The olympics has been hosted in this country \n Try now ")
    question1 = input ("What is the capital of china?\n 1. Bangkok\n 2. Beijing \n 3. Washington DC \n 4. Shanghai \n Your answer: ")

if question1 == "Beijing":
    score = score + 1
    print ("Correct, you have",score,"point")
elif question1 != "Beijing":
    print ("Incorrect, the correct answer was Beijing!")
    score = score + 0
question2 = input ("What is always with you but not always seen? \n 1. Your voice \n 2. The past \n 3. Your shadow \n 4. The future \n Your answer:")

if question2 == "hint":
    print ("It works better in the sun \n Try now")
    question2 = input ("What is always with you but not always seen? \n 1. Your voice \n 2. The past \n 3. Your shadow \n 4. The future \n Your answer:")

if question2 == "Your shadow":
    score = score + 1
    print ("Correct, you're getting there!")
elif question2 != "Your shadow":
    score = score + 0
    print ("That is not correct! Keep going! The correct answer was Your shadow")

question3 = input ("Steve Jobs founded which famous company in 1976 \n Apple \n Android \n Google \n Walmart \n Your answer: ")

if question3 == "hint":
    print ("You most likely own one of these products \n Try now")
    question3 = input ("Steve Jobs founded which famous company in 1976 \n 1. Apple \n 2. Android \n 3. Google \n 4. Walmart \n Your answer: ")

if question3 == "Apple":
    score = score + 1
    print ("Correct, you're nearly halfway there!")
elif question3 != "Apple":
    score = score + 0
    print ("Incorrect! The correct answer was Apple")

question4 = input ("Which of thew traditional five sens are dolphins believed not to have? \n 1. Smell \n 2. Taste \n 3. Sight \n 4. Touch \n Your answer:")

if question4 == "hint":
    print ("Some people say they would love to lose this sense. \n Try now ")
    question4 = input ("Which of thew traditional five sens are dolphins believed not to have? \n 1. Smell \n 2. Taste \n 3. Sight \n 4. Touch \n Your answer:")

if question4 == "Smell":
    score = score + 1
    print ("Correct, you're halfway there and you've scored" ,score, "points!")
elif question4 != "Smell":
    score = score + 0
    print ("Not quite, the correct answer was the sense of smell. We're halfway through and you've scored" ,score,"points")

question5 = input ("Which animal is proven  to have the biggest ears? \n 1. Whale \n 2. African Elephant \n 3. Bat-eared fox \n 4. Fennec Fox \n Your answer: ")

if question5 == "hint":
    print ("This animal is usually very friendly with humans")
    question5 = input ("Which animal is proven  to have the biggest ears? \n 1. Whale \n 2. African Elephants \n 3. Bat-eared fox \n 4. Fennec Fox \n Your answer:")

if question5 == "African Elephant":
    score = score + 1
    print ("Correct, most people think it is the Bat-eared fox but they would be wrong.")
elif question5 != "African Elephant":
    score = score + 0
    print ("Ouch, not quite. The correct answer was the African Elephant.")

question6 = input ("In WWE, what is John Cena's famous catchphrase? \n 1. 'It doesn't matter what you think \n 2. 'You’re FIIIIIRED!' \n 3. 'You can't see me' \n 4. 'Know your role, and shut your mouth!' \n Your answer: ")

if question6 == "hint":
    print ("Knowing that John Cena is cocky, which quote do you think would fit him the best? \n Try now.")
    question6 = input ("In WWE, what is John Cena's famous catchphrase? \n 1. 'It doesn't matter what you think \n 2. 'You’re FIIIIIRED!' \n 3. 'You can't see me' \n 4. 'Know your role, and shut your mouth!' \n Your answer: ")

if question6 == "You can't see me":
    score = score + 1
    print ("Correct, you are now on" ,score, "points ")
elif question6 != "You can't see me":
    score = score + 0
    print ("Oh jeez rick, i don't know if he knows. The correct answer was 'You can't see me'")

question7 = input ("Which tennis player has won the most men's Grand Slam titles? \n 1. Andy Murray \n 2. Roger Federer \n 3. Novak Djokovic \n 4. Rafael Nadal \n Your answer:  ")

if question7 == "hint":
    print ("This person is within the top 3 of the worlds best at the minute. \n Try now.")
    question6 = input ("Which tennis player has won the most men's Grand Slam titles? \n 1. Andy Murray \n 2. Roger Federer \n 3. Novak Djokovic \n 4. Rafael Nadal \n Your answer:  ")

if question7 == "Roger Federer":
    score = score + 1
    print ("Correct, you have " ,score, "points ")
elif question7 != "Roger Federer":
    score = score + 0
    print ("Incorrect, the correct answer was Roger Federer. You have ",score, "points")

question8 = input ("What is 'The Rock's' full name? \n 1. Dwayne Jonstone \n 2. Dwayne Joninston \n 3. Dwayne Johnstone \n 4.  Dwayne Douglas \n Your answer: ")

if question8 == "hint":
    print ("It was one spelling of the same word \n Try now.")
    question6 = input ("What is 'The Rock's' full name? \n 1. Dwayne Jonstone \n 2. Dwayne Joninston \n 3. Dwayne Johnstone \n 4.  Dwayne Douglas \n Your answer: ")

if question8 == "Dwayne Johnstone":
    score = score + 1
    print ("Correct, the rock's middle name is actually Douglas. You now have " ,score, "points ")
elif question6 != "Dwayne Johnstone":
    score = score + 0
    print ("Incorrect, it is 'Dwayne Johnstone")

question9 = input ("Which country won the 2012 UEFA European Championship?")

if question9 == "hint":
    print ("This place is a tourist attraction \n Try now.")
    question9 = input ("Which country won the 2012 UEFA European Championship?")

if question9 == "Spain":
    score = score + 1
    print ("Correct, you are now on" ,score, "points ")
elif question9 != "Spain":
    score = score + 0
    print ("That is the wrong answer, the correct answer is Spain!")


print ("You scored",score, "points.")
