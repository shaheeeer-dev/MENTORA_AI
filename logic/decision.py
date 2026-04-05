import json
from models.generator import ask_ai
from scraper.wiki_scraper import get_wiki_summary

with open('data/dictionary.json', 'r') as t:
    dictionary = json.load(t)

def normalize(text):
    text = text.lower()

    replacements = {
        "define" : "what is",
        "explain" : "what is",
        "describe" : "what is",
    }

    for i, j in replacements.items():
        text = text.replace(i, j)

    return text.strip()

def get_response(user_input):
    user_input = normalize(user_input)

    if user_input in dictionary:
        return dictionary[user_input]
    
    wiki_result = get_wiki_summary(user_input)
    if wiki_result:
        return wiki_result
    
    return ask_ai(user_input)