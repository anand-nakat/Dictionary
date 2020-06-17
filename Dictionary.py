import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean '%s' instead??" %get_close_matches(word, data.keys())[0])
        decide = input("Press y or n:")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("Doesn't look like a Word!!")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("Punched wrong keys,ha??")



word = input("Enter the word you want to search for: ")
output = translate(word)
if type(output) == list:
    i=1
    for item in output:
        print(str(i)+".",item)
        i+=1
else:
    print(output)




