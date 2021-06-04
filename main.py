import json
import difflib
import keyword
from difflib import get_close_matches
data = json.load(open("data.json"))

def suggest(b):
    try:
        similarword=get_close_matches(b,data.keys(),n=1,cutoff=0.8)[0]
        choice= input("did you mean "+similarword+" ?  (y or n) : ")
        if choice == "y":
            solution = data[similarword]
            for items in solution:
                 print("\n"+items)
            return "Thank You!"

        elif choice == "n":
            return "Then please enter correct word!"
        else:
            return "We don't understand your output."
    except:
        return "No such word exist"

def word(a):
        if a in data:
            meaning=data[a]
            return meaning
        elif a.lower() in data:
            meaning=data[a.lower()]
            return meaning
        elif a.title() in data:
            meaning=data[a.title()]
            return meaning
        else:
            return suggest(a)

user = input("provide a word for meaning:")
output = word(user)
for items in output:
    print("\n"+items)
