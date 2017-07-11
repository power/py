#Grade boundaries 
# 0 - 10 marks is a E
# 10 - 20 marks is a D
# 20 - 30 marks is a C
# 30 - 40 marks is a B
# 40 - 55 marks is an A
# 55 - 60 marks is an A*
score = float(input("What marks did you get you on your test?"))
if score <= 10:
    grade = "E"
elif score <= 20:
    grade = "D"
elif score <= 30:
    grade = "C"
elif score <= 40:
    grade = "B"
elif score <= 55:
    grade = "A"
elif score <= 60:
    grade = "A*"
elif score >= 60:
    print ("You have entered an invalid number, please try again.")

if grade == "E":
    leftovers = 10 - score
if grade == "D":
    leftovers = 20 - score
if grade == "C":
    leftovers = 30 - score
if grade == "B":
    leftovers = 40 - score
if grade == "A":
    leftovers = 55 - score
if grade == "A*":
    leftovers = 60 - score
print ("You needed",leftovers, "marks before you could reach your next grade")
