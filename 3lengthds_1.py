length1 = int(input("Please input an angle."))
length2 = int(input("Please input an angle."))
length3 = int(input("Please input an angle."))

if length1 == length2 or length2 == length3 or length1 == length3:
    print ("This is an isosceles triangle.")
else:
    print ("This is not an isosceles triangle.")
