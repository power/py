s = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY" # Currently raw string not within a list.
s = s.split(" ") # This is doing 2 things. The first is making it into a list and the second is spacing it out by putting a space (a comma) between every word.
unique = [] # This setting an empty list which is used later on
for letter in s: #Letter is defined by looking in S.
    if not letter in unique: # If the word in letter is not in unique. Append it. This will print the place of where it is
        unique.append(letter) # This is adding the numbers 
    print(letter) # Prints variable "letter"
    print(unique) # Prints variable "unique"

for letter in s: # If letter and s contain the same string
    print(unique.index(letter)) # Print the place of the word.
    
