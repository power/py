workerhour = float(input("Please input the number of hours a worker has worked in a week"))
workermoney = float(input("Please input the amount of money a worker earns in a week"))
# Asks the user for the amount of hours and money they own in a week
answer=int(workerhour*workermoney)
# Times' both then prints the answer out
print (answer)

tax = answer + 0
tax2 = answer / 10 * 2
tax3 = answer/ 10 * 4
tax4 = answer / 10 * 5
insurance = tax * 0.8
insurance2 = tax2 * 0.8
insurance3 = tax3 * 0.8
insurance4 = tax4 * 0.8


if workermoney < 11000:
    print (tax,"this is how much you earn per year with a 0% tax.")
elif workermoney < 45000:
    print (tax2,"this is how much you earn per year with a 20% tax.")
elif workermoney > 45000:
    print (tax3,"this is how much you earn per year with a 40% tax.")
elif workermoney > 50000:
    print (tax4,"this is how much you earn per year with a 40% tax.")
print (insurance)
print (insurance2)
print (insurance3)
print (insurance4)

answer2 = answer / 2
answer3 = answer2 + answer
print ("If you worked overtime you would earn",answer3,"extra")
