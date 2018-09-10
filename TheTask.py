sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU BUT WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence_list = sentence.split(" ")
print (sentence_list)
for word in sentence_list:
    print (word)
userInput = input("From the sentence printed above, is there a word you would like to search for?").upper()

if userInput in sentence:
    print ("Nice! We found your word.")
else:
    print ("We could not find your word.")

userRestart = input("Would you like to search for another word?")

if userRestart == "yes":
    userInput = input("Pick another word from the sentence that was first printed.")
if userInput in sentence:
    print ("Nice we found your word.")
else:
    print ("We could not find your word.")
    
if userRestart == "no":
    end2 = input("Thank you for using this program. Press any button to end.")
else:
    end2 = input ("You sent an invalid string! Please respond with yes or no")

if userRestart == "yes" and userInput in sentence:
    print ("Nice! We found your word")
else:
    input()
