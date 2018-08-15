import re
import string

def word_count(phrase):
    d = {}
    for w in re.split('[\s.,_]+', phrase):
        word = w.lower().strip(string.punctuation)
        if word == '':
            continue
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

