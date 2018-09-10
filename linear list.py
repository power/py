def linearSearch(myItem,myList):#Defining muliple functions (myItem and myList)
    found = False # Setting the variable "found" to default as "False"
    position = 0 # Setting the variable "position" to default as "0"
        while position < len(myList) and not found: # Whilst the position is not in the list and found is false
        if myList[position] == myItem: # If myList variable with the place of 0 is equal to the user item
            found = True # Reset the found variable to true.
        position = position+1 # Position goes up by one if the program doesnt work/
    return found 


if __name__=="__main__": 
    shopping = ["apples","bananas","chocolate","pasta"] # Defining a list including some items that will be searched for later.
    item = input("What item do you want to find?") # Asks the user what they want to find
    isitFound =linearSearch(item,shopping) # Run the linearSearch aswell as the list and input 
    if isitFound: # If the users input is in the list print that it is.
        print ("Your item is in the list!") 
    else: # Otherwise print that it is not.
        print ("Your item is not in the list")
