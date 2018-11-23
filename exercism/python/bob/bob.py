import re


def hey(phrase):
    phrase = re.sub(r'\s', '', phrase)
    if not phrase:
        return 'Fine. Be that way!'

    is_question = phrase.endswith('?')

    letters = list(filter(lambda x: x.isalpha(), phrase)) 
    is_shouting = letters and all(map(str.isupper, letters))

    if is_question and is_shouting:
        return "Calm down, I know what I'm doing!"

    if is_question:
        return 'Sure.'

    if is_shouting:
        return 'Whoa, chill out!'
    
    return 'Whatever.'
