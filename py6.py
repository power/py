monthnumber = 0
whatmonth = str(input("What Month Are You In?"))
#LOWERCASE
if whatmonth == "january":
    monthnumber = monthnumber + 1
elif whatmonth == "february":
    monthnumber = monthnumber + 2
elif whatmonth == "march":
    monthnumber = monthnumber + 3
elif whatmonth == "april":
    monthnumber = monthnumber + 4
elif whatmonth == "may":
    monthnumber = monthnumber + 5
elif whatmonth == "june":
    monthnumber = monthnumber + 6
elif whatmonth == "july":
    monthnumber = monthnumber + 7
elif whatmonth == "august":
    monthnumber = monthnumber + 8
elif whatmonth == "september":
    monthnumber = monthnumber + 9
elif whatmonth == "october":
    monthnumber = monthnumber + 10
elif whatmonth == "november":
    monthnumber = monthnumber + 11
    #UPPERCASE
elif whatmonth == "January":
    monthnumber = monthnumber + 1    
elif whatmonth == "February":
    monthnumber = monthnumber + 2
elif whatmonth == "March":
    monthnumber = monthnumber + 3
elif whatmonth == "April":
    monthnumber = monthnumber + 4
elif whatmonth == "May":
    monthnumber = monthnumber + 5
elif whatmonth == "June":
    monthnumber = monthnumber + 6
elif whatmonth == "July":
    monthnumber = monthnumber + 7
elif whatmonth == "August":
    monthnumber = monthnumber + 8
elif whatmonth == "September":
    monthnumber = monthnumber + 9
elif whatmonth == "october":
    monthnumber = monthnumber + 10
elif whatmonth == "november":
    monthnumber = monthnumber + 11
elif whatmonth == "December":
    monthnumber = monthnumber + 12
else:
    monthnumber = monthnumber +12


if monthnumber == 1:
    print("you are in winter")
elif monthnumber == 2:
    print("you are in winter")
elif monthnumber == 3:
    print("you are in spring")
elif monthnumber == 4:
    print("you are in spring")
elif monthnumber == 5:
    print("you are in spring")
elif monthnumber == 6:
    print("you are in summer")
elif monthnumber == 7:
    print("you are in summer")
elif monthnumber == 8:
    print("you are in summer")
elif monthnumber == 9:
    print("you are in autumn")
elif monthnumber == 10:
    print("you are in autumn")
elif monthnumber == 11:
    print("you are in autumn")
else:
    print("you are in winter")
