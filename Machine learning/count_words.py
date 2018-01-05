"""count words without punctuations"""

import string
import re

def count_words(text):
    """count unique word occurrence"""
    counts = dict()

    # convert to lowercase
    text = text.lower()

    # remove punctuations
    # method 1 make table punctuations to " " 
    # table = str.maketrans(dict.fromkeys(string.punctuation, " "))
    # text = text.translate(table)
    
    # method 2 substitute characters who are not letters or numbers
    # to space
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)

    # split into tokens
    words = text.split()

    # aggregate word counts using a dictionary
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    return counts


text = "I,am a boy!"
print(count_words(text))
