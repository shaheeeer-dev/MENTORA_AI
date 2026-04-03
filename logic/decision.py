import json

with open('data/dictionary.json', 'r') as t:
    dictionary = json.load(t)

def normalize(text):
    text = text.lower()

    replacements = {
        "define" : "what is",
        "explain" : "what is",
        "describe" : "what is",
        "tell me about" : "what is",
        "give me info about": "what is"
    }

    for i, j in replacements.items():
        text = text.replace(i, j)

    return text.strip()

def get_response(user_input):
    user_input = normalize(user_input)

    if user_input in dictionary:
        return dictionary[user_input]
    
    return "I don't know yet."