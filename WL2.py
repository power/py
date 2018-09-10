random = "test" # On this line we are defining the word people will have to find out
guess = input("Guess a word, if you're correct, i'll give you a cookie!") # We are asking the user to input a word.
while guess != random: # Whilst the users guess is not equal to the variable we defined
    guess = input("Try again") # Re-set the users guess to whatever they will guess. 
if guess == random: # If the guess is equal to the word
    print ("Congratulations, you can have a cookie!") # Print they have won!
