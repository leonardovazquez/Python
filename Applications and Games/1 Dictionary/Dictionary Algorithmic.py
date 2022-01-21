# Dictionary Algorithmic
# This is a small project developed by Leonardo Vazquez.
# It uses a .json file to find word definitions. It also includes a checker.

# import libraries and modules
import json
from difflib import get_close_matches

# Open the .json file
data = json.load(open("Applications and Games/1 Dictionary/data.json"))


# Search function definition
def search(w):
    z = ["The word is not in the Dictionary"]
    # This is the checker.
    if w in data:
        print("\"", w, "\"")
        return data[w]
    elif w.title() in data:
        print("\"", w.title(), "\"")
        return data[w.title()]
    elif w.lower() in data:
        print("\"", w.lower(), "\"")
        return data[w.lower()]
    elif w.upper() in data:
        print("\"", w.upper(), "\"")
        return data[w.upper()]
    # The checker corrects the incorrectly entered word and searches for similar words:
    elif len(get_close_matches(w, data.keys())) > 0:
        print("did you mean \"", get_close_matches(w, data.keys())[0], "\" instead of \"", w, "\"")
        decide = input("press \"y\" for yes or \"n\" for no.")
        if decide == "y":
            print("\"", get_close_matches(w, data.keys())[0], "\"")
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return z
    else:
        return z


# The input and the function call
word = input("Enter the word: ")
output = search(word)

# The outputs
for i in output:
    print("-", i)



