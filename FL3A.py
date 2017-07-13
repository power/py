number = int(input("Give me a times tables")) # This line is asking for a full number and then saving it as a variable
multiplier = 0# The multiplier variable is saved as 0.

for counter in range (0 , 12): # Thisline is saying that it will count up from 0 until 12 repeating the code below
    multiplier = multiplier + 1 # We are now resaggining the variable called Multiplier to add 1 
    print(multiplier,"x",number,"=",number*multiplier)# At the start of the brackets it will print which number timesed by the value it is doing, so for example 2 * 7. After that it displays the value saved at the top of the code
    #After that it then does the calcuation and prints it on the screen 
