from collections import defaultdict


def is_isogram(string):
    d = defaultdict(int)
    for c in string.lower():
        if c in {' ', '-'}:
            continue
        d[c] += 1    
    return not d or max(d.values()) < 2
