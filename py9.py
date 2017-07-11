roadtype = input("Are you driving on a motorway, an A-road or through the town")
length = float(input("What is the distance you are travelling?"))
if roadtype == "motorway":
    print (length/70 ," this is how long in minutes it will take you to reach your distance")
elif roadtype == "a-road":
    print (length/70 ," this is how long in minutes it would take you to reach your destination")
elif roadtype == "town":
    print (length/30 ," this is how long in minutes it would take you to reach your destination")
elif roadtype == "Motorway":
    print (length/70 ," this is how long in minutes it will take you to reach your distance")
elif roadtype == "A-road":
    print (length/70 ," this is how long in minutes it would take you to reach your destination")
elif roadtype == "Town":
    print (length/30 ," this is how long in minutes it would take you to reach your destination")

if roadtype == "motorway":
    print ("You cannot go over 70 miles an hour when on these roads")
elif roadtype == "a-road":
    print ("You cannot go over 70 miles an hour when on these roads")
elif roadtype == "town":
    print ("You canot go over 30 miles an hour when on these roads")
elif roadtype == "Motorway":
    print ("You cannot go over 70 miles an hour when on these roads")
elif roadtype == "A-road":
    print ("You cannot go over 70 miles an hour when on these roads")
elif roadtype == "Town":
    print ("You canot go over 30 miles an hour when on these roads")
