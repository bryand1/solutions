from string import ascii_lowercase


def is_pangram(sentence):
    s = sentence.lower()
    return not (set(ascii_lowercase) - set(s))
