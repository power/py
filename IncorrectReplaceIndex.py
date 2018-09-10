sentence = "Red Green Blue"
sentence_list = sentence.split(" ")
R = "Red"
G = "Green"
B = "Blue"
if R in sentence:
    sentence_list = sentence.replace("Red","0")
elif G in sentence:
    sentence_list = sentence.replace ("Green", "1")
elif B in sentence:
    sentence_list = sentence.replace ("Blue", "2")
print (new_sentence)
