userAnswer = int(input("How old are you?"))

if userAnswer < 17:
    print ("You are not eligible to drive")
else:
    print ("You are eligible to drive")

userResponse = input ("Have you applied for enhanced rate of mobility?")

if userResponse == "Yes":
    print ("You are eligible to drive")
else:
    print ("You are not eligibile to drive")
